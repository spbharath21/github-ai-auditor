"""
Detects dangerous code execution patterns: eval, exec, subprocess, os.system.

These are flagged as LLM07 (Insecure Plugin Design) when they appear in
files that also use LLM/AI libraries - the concern is that LLM output
flows into these calls without sanitisation, letting an attacker run
arbitrary code by injecting into the prompt.

Even without LLM context, these are HIGH severity findings worth reporting.
"""

import re
from auditor.fetcher import RepoFile
from auditor.models import Finding, Severity

# Patterns that indicate dangerous execution
EXEC_PATTERNS: list[tuple[str, str, re.Pattern]] = [
    ("eval() with non-literal argument", "eval_usage",
     re.compile(r"\beval\s*\([^)]{3,}\)")),

    ("exec() call", "exec_usage",
     re.compile(r"\bexec\s*\([^)]{3,}\)")),

    ("os.system() call", "os_system",
     re.compile(r"\bos\.system\s*\(")),

    ("subprocess with shell=True", "subprocess_shell",
     re.compile(r"subprocess\.(run|Popen|call|check_output)\s*\([^)]*shell\s*=\s*True")),

    ("__import__ dynamic import", "dynamic_import",
     re.compile(r"__import__\s*\(")),
]

# If these imports are present in the file, we know it's an AI/LLM file
# and can bump the OWASP category to LLM07 specifically
LLM_IMPORT_SIGNALS = re.compile(
    r"(?i)(import openai|import anthropic|from langchain|import langchain|"
    r"from llama|import llama|from transformers|import transformers|"
    r"ChatOpenAI|AzureChatOpenAI|claude|gemini)"
)


def scan_unsafe_exec(file: RepoFile) -> list[Finding]:
    findings: list[Finding] = []
    lines = file.content.splitlines()

    # Check once per file if this is an AI/LLM-using file
    is_llm_file = bool(LLM_IMPORT_SIGNALS.search(file.content))
    owasp_id = "LLM07" if is_llm_file else None

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Skip comments
        if stripped.startswith("#") or stripped.startswith("//"):
            continue

        for label, category, pattern in EXEC_PATTERNS:
            if pattern.search(line):
                # subprocess shell=True is critical, rest are high
                severity = (
                    Severity.CRITICAL
                    if category == "subprocess_shell"
                    else Severity.HIGH
                )
                findings.append(Finding(
                    file=file.path,
                    line=line_num,
                    severity=severity,
                    category=category,
                    owasp_id=owasp_id,
                    message=f"Dangerous execution pattern: {label}",
                    snippet=line.strip()[:120],
                ))
                break  # one finding per line

    return findings