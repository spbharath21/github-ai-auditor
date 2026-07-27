"""
Converts a list of findings into a security score and OWASP summary.
"""

from dataclasses import dataclass, field
from auditor.models import Finding, Severity

# How many points each severity deducts from 100
DEDUCTIONS = {
    Severity.CRITICAL: 20,
    Severity.HIGH: 10,
    Severity.MEDIUM: 5,
    Severity.LOW: 2,
}

OWASP_DESCRIPTIONS = {
    "LLM01": "Prompt Injection",
    "LLM02": "Insecure Output Handling",
    "LLM03": "Training Data Poisoning",
    "LLM04": "Model Denial of Service",
    "LLM05": "Supply Chain Vulnerabilities",
    "LLM06": "Sensitive Information Disclosure",
    "LLM07": "Insecure Plugin Design",
    "LLM08": "Excessive Agency",
    "LLM09": "Overreliance",
    "LLM10": "Model Theft",
}


@dataclass
class ScanResult:
    score: int
    risk_level: str
    total_findings: int
    findings_by_severity: dict[str, int]
    owasp_coverage: dict[str, list[Finding]]  # LLM01 → [findings]
    findings: list[Finding]
    files_scanned: int = 0


def score_findings(findings: list[Finding], files_scanned: int = 0) -> ScanResult:
    score = 100
    for f in findings:
        score -= DEDUCTIONS.get(f.severity, 0)
    score = max(0, score)

    if score >= 80:
        risk_level = "Low"
    elif score >= 60:
        risk_level = "Medium"
    elif score >= 40:
        risk_level = "High"
    else:
        risk_level = "Critical"

    findings_by_severity: dict[str, int] = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for f in findings:
        findings_by_severity[f.severity.value] += 1

    # Group findings by OWASP category
    owasp_coverage: dict[str, list[Finding]] = {}
    for f in findings:
        if f.owasp_id:
            owasp_coverage.setdefault(f.owasp_id, []).append(f)

    return ScanResult(
        score=score,
        risk_level=risk_level,
        total_findings=len(findings),
        findings_by_severity=findings_by_severity,
        owasp_coverage=owasp_coverage,
        findings=findings,
        files_scanned=files_scanned,
    )