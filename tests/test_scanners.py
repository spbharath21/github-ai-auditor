"""
Unit tests for all 4 scanners using fake RepoFile objects.
No GitHub API calls needed - fast, offline, runnable anytime.
"""

from auditor.fetcher import RepoFile
from auditor.scanners.secrets import scan_secrets
from auditor.scanners.unsafe_exec import scan_unsafe_exec
from auditor.scanners.prompt_injection import scan_prompt_injection
from auditor.scanners.rag_safety import scan_rag_safety
from auditor.aggregator import run_all_scanners
from auditor.scoring import score_findings


def make_file(content: str, path: str = "test.py") -> RepoFile:
    return RepoFile(path=path, content=content, size_bytes=len(content))


# ── Secrets scanner ────────────────────────────────────────────────

def test_detects_openai_key():
    f = make_file('api_key = "sk-proj-aB3dEfGhIjKlMnOpQrStUvWxYz1234567890"')
    findings = scan_secrets(f)
    assert len(findings) == 1
    assert findings[0].owasp_id == "LLM06"
    assert findings[0].severity.value == "critical"

def test_detects_aws_key():
    f = make_file('AWS_KEY = "AKIAQZ7MKTESTKEY1234"')
    findings = scan_secrets(f)
    assert len(findings) == 1

def test_ignores_placeholder():
    f = make_file('api_key = "your_api_key_here"')
    findings = scan_secrets(f)
    assert len(findings) == 0

def test_detects_high_entropy_password():
    f = make_file('db_password = "xK9$mPz#2qLwVnR8tY5j"')
    findings = scan_secrets(f)
    assert len(findings) == 1
    assert findings[0].severity.value == "high"

def test_ignores_low_entropy_password():
    f = make_file('secret_token = "password123"')
    findings = scan_secrets(f)
    assert len(findings) == 0


# ── Unsafe exec scanner ────────────────────────────────────────────

def test_detects_eval():
    f = make_file('result = eval(user_input)')
    findings = scan_unsafe_exec(f)
    assert len(findings) == 1
    assert "eval" in findings[0].message

def test_detects_subprocess_shell():
    f = make_file('subprocess.run(cmd, shell=True)')
    findings = scan_unsafe_exec(f)
    assert len(findings) == 1
    assert findings[0].severity.value == "critical"

def test_ignores_commented_eval():
    f = make_file('# eval(user_input)  -- dont use this')
    findings = scan_unsafe_exec(f)
    assert len(findings) == 0


# ── Prompt injection scanner ───────────────────────────────────────

def test_detects_user_input_to_llm():
    code = '''
user_input = input("Enter query: ")
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": user_input}]
)
'''
    f = make_file(code)
    findings = scan_prompt_injection(f)
    assert len(findings) >= 1
    assert findings[0].owasp_id == "LLM01"

def test_no_finding_without_user_input():
    code = '''
prompt = "Summarize this document"
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
'''
    f = make_file(code)
    findings = scan_prompt_injection(f)
    assert len(findings) == 0


# ── RAG safety scanner ─────────────────────────────────────────────

def test_detects_unsafe_rag():
    code = '''
from langchain.vectorstores import Chroma
docs = vectorstore.similarity_search(query)
response = chain.invoke(docs)
'''
    f = make_file(code)
    findings = scan_rag_safety(f)
    assert len(findings) >= 1
    assert findings[0].owasp_id == "LLM01"

def test_no_rag_finding_without_langchain():
    code = '''
docs = db.search(query)
result = process(docs)
'''
    f = make_file(code)
    findings = scan_rag_safety(f)
    assert len(findings) == 0


# ── Scoring ────────────────────────────────────────────────────────

def test_perfect_score_no_findings():
    result = score_findings([], files_scanned=10)
    assert result.score == 100
    assert result.risk_level == "Low"

def test_score_deducts_correctly():
    f = make_file('api_key = "sk-proj-aB3dEfGhIjKlMnOpQrStUvWxYz1234567890"')
    findings = run_all_scanners([f])
    result = score_findings(findings)
    assert result.score < 100
    assert result.findings_by_severity["critical"] >= 1