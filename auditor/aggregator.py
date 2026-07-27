"""
Runs all scanners against all files and combines results.

Why a separate aggregator: the CLI and the report generator don't need to
know which scanners exist. You can add a 5th scanner by importing it here
and adding one line - nothing else changes.
"""

from auditor.fetcher import RepoFile
from auditor.models import Finding
from auditor.scanners.secrets import scan_secrets
from auditor.scanners.unsafe_exec import scan_unsafe_exec
from auditor.scanners.prompt_injection import scan_prompt_injection
from auditor.scanners.rag_safety import scan_rag_safety


def run_all_scanners(files: list[RepoFile]) -> list[Finding]:
    """
    Runs every scanner on every file. Returns all findings, sorted by
    severity (critical first) then by file path for consistent output.
    """
    all_findings: list[Finding] = []

    for file in files:
        all_findings.extend(scan_secrets(file))
        all_findings.extend(scan_unsafe_exec(file))
        all_findings.extend(scan_prompt_injection(file))
        all_findings.extend(scan_rag_safety(file))

    # Sort: critical → high → medium → low, then by file path
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    all_findings.sort(
        key=lambda f: (severity_order.get(f.severity.value, 99), f.file, f.line)
    )

    return all_findings