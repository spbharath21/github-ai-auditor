"""
Detects prompt injection: user-controlled input flowing into LLM calls without sanitisation.
Maps to OWASP LLM01.
"""

import re
from auditor.fetcher import RepoFile
from auditor.models import Finding, Severity

LLM_CALL_PATTERNS = [
    re.compile(r"openai\.chat\.completions\.create"),
    re.compile(r"client\.chat\.completions\.create"),
    re.compile(r"openai\.ChatCompletion\.create"),
    re.compile(r"anthropic\.messages\.create"),
    re.compile(r"client\.messages\.create"),
    re.compile(r"\.invoke\s*\("),
    re.compile(r"\.run\s*\("),
    re.compile(r"pipeline\s*\("),
    re.compile(r"generate\s*\("),
]

USER_INPUT_PATTERNS = [
    re.compile(r"\brequest\.(args|form|json|data|get)\b"),
    re.compile(r"\binput\s*\("),
    re.compile(r"\buser_input\b"),
    re.compile(r"\buser_message\b"),
    re.compile(r"\buser_query\b"),
    re.compile(r"\buser_prompt\b"),
    re.compile(r"\bprompt\s*=.*input"),
    re.compile(r"sys\.argv"),
]

SANITISATION_PATTERNS = [
    re.compile(r"(?i)(sanitize|sanitise|validate|escape|strip|bleach|clean)"),
    re.compile(r"(?i)(moderation|content.?filter|guard|guardrail)"),
]

# Only scan Python/JS/TS files — not YAML, markdown, or config files
SCANNABLE_EXTENSIONS = re.compile(r"\.(py|js|ts|jsx|tsx)$")

CONTEXT_WINDOW = 15


def _has_sanitisation(lines: list[str], center: int, window: int) -> bool:
    start = max(0, center - window)
    end = min(len(lines), center + window)
    context = "\n".join(lines[start:end])
    return any(p.search(context) for p in SANITISATION_PATTERNS)


def scan_prompt_injection(file: RepoFile) -> list[Finding]:
    # Only scan actual code files
    if not SCANNABLE_EXTENSIONS.search(file.path):
        return []

    findings: list[Finding] = []
    lines = file.content.splitlines()

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("#") or stripped.startswith("//"):
            continue

        is_llm_call = any(p.search(line) for p in LLM_CALL_PATTERNS)
        if not is_llm_call:
            continue

        start = max(0, line_num - 1 - CONTEXT_WINDOW)
        end = min(len(lines), line_num + CONTEXT_WINDOW)
        context = "\n".join(lines[start:end])

        if not any(p.search(context) for p in USER_INPUT_PATTERNS):
            continue

        if _has_sanitisation(lines, line_num - 1, CONTEXT_WINDOW):
            findings.append(Finding(
                file=file.path,
                line=line_num,
                severity=Severity.LOW,
                category="prompt_injection_possible",
                owasp_id="LLM01",
                message="LLM call near user input — sanitisation detected but verify it's sufficient",
                snippet=line.strip()[:120],
            ))
        else:
            findings.append(Finding(
                file=file.path,
                line=line_num,
                severity=Severity.HIGH,
                category="prompt_injection_likely",
                owasp_id="LLM01",
                message="LLM call with nearby user input and no visible sanitisation",
                snippet=line.strip()[:120],
            ))

    return findings