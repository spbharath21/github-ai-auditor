import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from auditor.fetcher import collect_repository_files
from auditor.aggregator import run_all_scanners
from auditor.scoring import score_findings
from auditor.report import print_terminal_report, generate_markdown_report

console = Console()


@click.group()
def main():
    """GitHub AI Security Auditor — scan repos for OWASP LLM Top 10 issues."""
    pass


@main.command()
@click.option("--repo", required=True, help="GitHub repo: owner/repo or full URL")
@click.option("--output", default=None, help="Save markdown report to this file")
@click.option("--verbose", is_flag=True, help="Show each file as it's fetched")
@click.option("--max-files", default=0, help="Stop after scanning this many files (0 = no limit)")
def scan(repo: str, output: str | None, verbose: bool, max_files: int):
    """Scan a GitHub repository for AI/LLM security issues."""

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,     # clears the spinner line once done
    ) as progress:

        task = progress.add_task(f"Fetching files from {repo} ...", total=None)

        try:
            files = collect_repository_files(repo, max_files=max_files)
        except Exception as e:
            console.print(f"[bold red]Error fetching repo:[/bold red] {e}")
            return

        progress.update(task, description=f"Running scanners on {len(files)} files ...")

        if not files:
            console.print("[yellow]No scannable files found.[/yellow]")
            return

        if verbose:
            for f in files:
                console.print(f"  [dim]scanning[/dim] {f.path}")

        findings = run_all_scanners(files)
        result = score_findings(findings, files_scanned=len(files))

    # Progress spinner is gone by here — print the clean report
    print_terminal_report(result, repo)

    if output:
        md = generate_markdown_report(result, repo)
        with open(output, "w", encoding="utf-8") as f:
            f.write(md)
        console.print(f"\n[green]Report saved to:[/green] {output}")