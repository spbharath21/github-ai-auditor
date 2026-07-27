import math
import re
from auditor.fetcher import RepoFile
from auditor.models import Finding, Severity

SECRET_PATTERNS: list[tuple[str, str, re.Pattern]] = [
    ("OpenAI API key",              "openai",       re.compile(r"sk-(proj-)?[A-Za-z0-9_\-]{20,}")),
    ("Anthropic API key",           "anthropic",    re.compile(r"sk-ant-[A-Za-z0-9\-]{20,}")),
    ("AWS Access Key ID",           "aws",          re.compile(r"AKIA[0-9A-Z]{16}")),
    ("Hugging Face token",          "huggingface",  re.compile(r"hf_[A-Za-z0-9]{30,}")),
    ("GitHub Personal Access Token","github",       re.compile(r"ghp_[A-Za-z0-9]{36}")),
    ("Generic API key assignment",  "generic",
     re.compile(r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*[\"'][A-Za-z0-9_\-]{16,}[\"']")),
]

SUSPICIOUS_VAR_NAME = re.compile(
    r"(?i)(password|passwd|pwd|secret|token|api_?key|auth)"
)

PLACEHOLDER_PATTERN = re.compile(
    r"(?i)(your[_-]?api[_-]?key|xxx+|placeholder|<.*?>|\$\{.*?\}|change[_-]?me|todo|fake|mock|dummy|sample|test[_-]?key|example[_-]?key)"
)

# Don't scan YAML workflow files for secrets — too many false positives
# from shell scripts, error messages, and CI variable references
SKIP_FILE_PATTERN = re.compile(r"\.(yml|yaml)$")

# Test files: still run known-pattern detection (real keys in tests = real risk)
# but skip entropy analysis since fake mock strings look high-entropy by design
TEST_FILE_PATTERN = re.compile(r"(test_|_test\.py|/tests/|\\tests\\)")

def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    freq: dict[str, int] = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    entropy = 0.0
    length = len(s)
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy


def _extract_quoted_value(line: str) -> str | None:
    match = re.search(r"[\"']([^\"']{8,})[\"']", line)
    return match.group(1) if match else None


def scan_secrets(file: RepoFile) -> list[Finding]:
    # Skip YAML files — shell scripts and CI configs generate too many false positives
    if SKIP_FILE_PATTERN.search(file.path):
        return []

    findings: list[Finding] = []
    lines = file.content.splitlines()

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Skip comments
        if stripped.startswith("#") or stripped.startswith("//"):
            continue

        if PLACEHOLDER_PATTERN.search(line):
            continue

        # Strategy 1: known service patterns
        for service_label, _, pattern in SECRET_PATTERNS:
            if pattern.search(line):
                findings.append(Finding(
                    file=file.path,
                    line=line_num,
                    severity=Severity.CRITICAL,
                    category="hardcoded_secret",
                    owasp_id="LLM06",
                    message=f"Hardcoded {service_label} detected",
                    snippet=line.strip()[:120],
                ))
                break
        else:
            # Strategy 2: entropy fallback — skip for test files
            # Test files use fake high-entropy strings as mock data by design
            if not TEST_FILE_PATTERN.search(file.path):
                if SUSPICIOUS_VAR_NAME.search(line):
                    value = _extract_quoted_value(line)
                    if value and shannon_entropy(value) > 4.0:
                        findings.append(Finding(
                            file=file.path,
                            line=line_num,
                            severity=Severity.HIGH,
                            category="possible_hardcoded_secret",
                            owasp_id="LLM06",
                            message="High-entropy string in a credential-like variable",
                            snippet=line.strip()[:120],
                        ))

    return findings