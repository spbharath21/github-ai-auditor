"""
Detects unsafe RAG implementations — retrieval results fed to LLMs without sanitisation.
Maps to OWASP LLM01.
"""

import re
from auditor.fetcher import RepoFile
from auditor.models import Finding, Severity

# Only flag actual retrieval *calls*, not imports/type annotations/comments
RETRIEVAL_CALL_PATTERNS = [
    re.compile(r"\.\s*similarity_search\s*\("),        # .similarity_search(
    re.compile(r"\.\s*asimilarity_search\s*\("),       # async variant
    re.compile(r"\.\s*max_marginal_relevance_search\s*\("),
    re.compile(r"retriever\.get_relevant_documents\s*\("),
    re.compile(r"retriever\.ainvoke\s*\("),
    re.compile(r"\.retrieve\s*\("),
    re.compile(r"RetrievalQA\.from_chain_type\s*\("),
    re.compile(r"ConversationalRetrievalChain\.from_llm\s*\("),
]

SANITISATION_SIGNALS = [
    re.compile(r"(?i)(filter|validate|sanitize|sanitise|clean|strip|escape)"),
    re.compile(r"(?i)(content.?filter|moderation|guardrail|guard)"),
]

# Skip test files - they call retrieval APIs by design
TEST_FILE_PATTERN = re.compile(r"(test_|_test\.py|tests/|/test/)")

CONTEXT_WINDOW = 10


def scan_rag_safety(file: RepoFile) -> list[Finding]:
    # Only scan files with langchain/vector store imports
    if not re.search(r"(?i)(langchain|chromadb|pinecone|weaviate|faiss|qdrant|pgvector)", file.content):
        return []

    # Skip test files — they legitimately call similarity_search without sanitisation
    if TEST_FILE_PATTERN.search(file.path):
        return []

    # Only scan Python files — not YAML, not markdown
    if not file.path.endswith((".py", ".ts", ".js")):
        return []

    findings: list[Finding] = []
    lines = file.content.splitlines()

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Skip comments and import lines
        if stripped.startswith("#") or stripped.startswith("from ") or stripped.startswith("import "):
            continue

        is_retrieval_call = any(p.search(line) for p in RETRIEVAL_CALL_PATTERNS)
        if not is_retrieval_call:
            continue

        start = max(0, line_num - 1 - CONTEXT_WINDOW)
        end = min(len(lines), line_num + CONTEXT_WINDOW)
        context = "\n".join(lines[start:end])

        has_sanitisation = any(p.search(context) for p in SANITISATION_SIGNALS)

        findings.append(Finding(
            file=file.path,
            line=line_num,
            severity=Severity.MEDIUM if has_sanitisation else Severity.HIGH,
            category="unsafe_rag",
            owasp_id="LLM01",
            message=(
                "RAG retrieval call — verify retrieved content is sanitised before LLM injection"
                if has_sanitisation
                else "RAG retrieval call with no visible sanitisation of retrieved content"
            ),
            snippet=line.strip()[:120],
        ))

    return findings