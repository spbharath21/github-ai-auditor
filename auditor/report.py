"""
Generates terminal output and markdown reports from a ScanResult.
"""

import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from rich.console import Console
from rich.table import Table
from rich import box

from auditor.scoring import ScanResult, OWASP_DESCRIPTIONS

console = Console()

SEVERITY_COLORS = {
    "critical": "bold red",
    "high": "red",
    "medium": "yellow",
    "low": "dim",
}

# Path to the templates/ folder — works regardless of where the CLI is run from
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


def print_terminal_report(result: ScanResult, repo: str) -> None:
    console.print(f"\n[bold]GitHub AI Security Auditor[/bold] — [cyan]{repo}[/cyan]")
    console.print(f"Files scanned: {result.files_scanned}  |  Findings: {result.total_findings}\n")

    score_color = {"Low": "green", "Medium": "yellow", "High": "red", "Critical": "bold red"}[result.risk_level]
    console.print(f"[bold]Security Score:[/bold] [{score_color}]{result.score}/100 — {result.risk_level} Risk[/{score_color}]\n")

    if not result.findings:
        console.print("[green]No issues found.[/green]")
        return

    table = Table(box=box.SIMPLE_HEAVY, show_lines=False)
    table.add_column("Severity", width=9)
    table.add_column("OWASP", width=7)
    table.add_column("File", style="cyan", max_width=40)
    table.add_column("Line", width=5, justify="right")
    table.add_column("Message")

    for f in result.findings:
        sev = f.severity.value
        color = SEVERITY_COLORS.get(sev, "white")
        table.add_row(
            f"[{color}]{sev.upper()}[/{color}]",
            f.owasp_id or "—",
            f.file,
            str(f.line),
            f.message,
        )

    console.print(table)

    if result.owasp_coverage:
        console.print("\n[bold]OWASP LLM Top 10 Coverage:[/bold]")
        for owasp_id, owasp_findings in sorted(result.owasp_coverage.items()):
            desc = OWASP_DESCRIPTIONS.get(owasp_id, "Unknown")
            console.print(f"  [{owasp_id}] {desc} — {len(owasp_findings)} finding(s)")


def generate_markdown_report(result: ScanResult, repo: str) -> str:
    """
    Renders the markdown report using the Jinja2 template.
    Falls back to inline generation if the template file isn't found.
    """
    template_path = TEMPLATES_DIR / "report.md.j2"

    if template_path.exists():
        env = Environment(
            loader=FileSystemLoader(str(TEMPLATES_DIR)),
            autoescape=False,   # markdown doesn't need HTML escaping
        )
        template = env.get_template("report.md.j2")
        return template.render(result=result, repo=repo, owasp=OWASP_DESCRIPTIONS)

    # Fallback: plain string generation if template is missing
    lines = [
        f"# AI Security Audit Report\n",
        f"**Repository:** {repo}  ",
        f"**Files Scanned:** {result.files_scanned}  ",
        f"**Security Score:** {result.score}/100 — {result.risk_level} Risk  ",
        f"**Total Findings:** {result.total_findings}\n",
    ]
    for f in result.findings:
        lines.append(f"### [{f.severity.value.upper()}] {f.message}")
        lines.append(f"- **File:** `{f.file}` (line {f.line})")
        if f.owasp_id:
            lines.append(f"- **OWASP:** {f.owasp_id}")
        lines.append(f"\n```\n{f.snippet}\n```\n")
    return "\n".join(lines)