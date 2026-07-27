# AI Security Audit Report

**Repository:** hwchase17/langchain  
**Files Scanned:** 2580  
**Security Score:** 0/100 — Critical Risk  
**Total Findings:** 1240

## Summary

| Severity | Count |
|----------|-------|
| Critical | 4 |
| High | 1115 |
| Medium | 119 |
| Low | 2 |

## OWASP LLM Top 10 Mapping

### LLM01 — Prompt Injection
876 finding(s)

### LLM06 — Sensitive Information Disclosure
358 finding(s)

### LLM07 — Insecure Plugin Design
5 finding(s)


## Findings

### [CRITICAL] Hardcoded OpenAI API key detected
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_pii.py` (line 539)
- **Category:** hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
state = AgentState[Any](messages=[HumanMessage("Key: sk-abcdefghijklmnopqrstuvwxyz123456")])
```

### [CRITICAL] Hardcoded OpenAI API key detected
- **File:** `libs/langchain_v1/tests/unit_tests/agents/test_create_agent_tool_validation.py` (line 294)
- **Category:** hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"api_key": "sk-secret-key-abc123xyz",
```

### [CRITICAL] Hardcoded Generic API key assignment detected
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/conftest.py` (line 87)
- **Category:** hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
access_token="vcr-fake-access-token",  # noqa: S106
```

### [CRITICAL] Hardcoded OpenAI API key detected
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 150)
- **Category:** hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
_build_model(**{field: "sk-should-not-be-allowed"})
```

### [HIGH] Dangerous execution pattern: exec() call
- **File:** `.github/workflows/close_unchecked_issues.yml` (line 68)
- **Category:** exec_usage

```
const headingMatch = headingRe.exec(body);
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `.github/workflows/pr_labeler.yml` (line 68)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
echo "::error::GitHub App token generation failed — cannot classify contributor"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `.github/workflows/pr_lint_trailer.yml` (line 164)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
'Edit the PR description and remove the offending line(s). The trailer is auto-inserted by some Claude-based authoring t
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/documents/base.py` (line 47)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# it has been adopted by enough VectorStore implementations.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 101)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class SemanticSimilarityExampleSelector(_VectorStoreExampleSelector):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 115)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
example_docs = self.vectorstore.similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 135)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
example_docs = await self.vectorstore.asimilarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 147)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 191)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 231)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class MaxMarginalRelevanceExampleSelector(_VectorStoreExampleSelector):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 280)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 326)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/__init__.py` (line 4)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
a `VectorStore` while avoiding duplicated content and over-writing content
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 23)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 248)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore | DocumentIndex,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 259)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
TypeError: If the `vector_store` is neither a `VectorStore` nor a
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 262)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(vector_store, VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 265)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
msg = "The delete operation to VectorStore failed."
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 274)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
f"Vectorstore should be either a VectorStore or a DocumentIndex. "
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 438)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if type(destination).delete == VectorStore.delete:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 439)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# Checking if the VectorStore has overridden the default delete method
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 447)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
f"Vectorstore should be either a VectorStore or a DocumentIndex. "
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 534)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(destination, VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 614)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore | DocumentIndex,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 617)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(vector_store, VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 620)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
msg = "The delete operation to VectorStore failed."
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 629)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
f"Vectorstore should be either a VectorStore or a DocumentIndex. "
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 779)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
type(destination).adelete == VectorStore.adelete
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 780)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
and type(destination).delete == VectorStore.delete
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 782)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# Checking if the VectorStore has overridden the default adelete or delete
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 790)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
f"Vectorstore should be either a VectorStore or a DocumentIndex. "
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/api.py` (line 884)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(destination, VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 28)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
written into a `VectorStore` and when they were written.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
To be supported, a `VectorStore` needs to only support the ability to add and
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 54)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record manager succeeds, but corresponding writing to `VectorStore` fails.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 463)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
The fields in this response are optional and whether the `VectorStore`
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 521)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
When an ID is specified and the content already exists in the `VectorStore`,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 523)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
does not exist, the upsert method should add the item to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 526)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
items: Sequence of documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 531)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
successfully added or updated in the `VectorStore` and the list of IDs that
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 538)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Add or update documents in the `VectorStore`. Async version of `upsert`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 544)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
When an ID is specified and the item already exists in the `VectorStore`,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 546)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
does not exist, the upsert method should add the item to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 549)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
items: Sequence of documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/indexing/base.py` (line 554)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
successfully added or updated in the `VectorStore` and the list of IDs that
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/language_models/base.py` (line 104)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Encode the text into token IDs using the fallback GPT-2 tokenizer."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/language_models/base.py` (line 108)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Using fallback GPT-2 tokenizer for token counting. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/language_models/base.py` (line 109)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Token counts may be inaccurate for non-GPT-2 models. "
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/langchain_core/language_models/llms.py` (line 524)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
yield self.invoke(input, config=config, stop=stop, **kwargs)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/language_models/model_profile.py` (line 52)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Maximum context window (tokens)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/messages/base.py` (line 115)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Examples: response headers, logprobs, token counts, model name."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/messages/utils.py` (line 1375)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"type": "text", "text": "This is the FIRST 4 token block."},
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/messages/utils.py` (line 1376)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"type": "text", "text": "This is the SECOND 4 token block."},
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/messages/utils.py` (line 1435)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
[{"type": "text", "text": "This is the FIRST 4 token block."}],
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/messages/utils.py` (line 1487)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"{type(actual_token_counter)}."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/messages/utils.py` (line 2400)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Wrapper for `count_tokens_approximately` that matches expected signature."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/output_parsers/openai_tools.py` (line 299)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Output parser received a `max_tokens` stop reason. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/output_parsers/openai_tools.py` (line 300)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"The output is likely incomplete—please increase `max_tokens` "
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/langchain_core/prompts/chat.py` (line 813)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
prompt_value = template.invoke(
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/langchain_core/prompts/chat.py` (line 887)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
prompt_value = template.invoke("Hello, there!")
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/langchain_core/prompts/chat.py` (line 889)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
# prompt_value = template.invoke({"user_input": "Hello, there!"})
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/langchain_core/tracers/log_stream.py` (line 62)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""List of LLM tokens streamed by this run, if applicable."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 8)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores.base import VST, VectorStore, VectorStoreRetriever
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores.in_memory import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 13)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"InMemoryVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 14)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreRetriever",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 19)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStore": "base",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 21)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreRetriever": "base",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/__init__.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"InMemoryVectorStore": "in_memory",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VST = TypeVar("VST", bound="VectorStore")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 43)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStore(ABC):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 54)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Run more texts through the embeddings and add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 57)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Iterable of strings to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 60)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
**kwargs: `VectorStore` specific parameters.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 66)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
List of IDs from adding the texts into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 72)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if type(self).add_documents != VectorStore.add_documents:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 193)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Async run more texts through the embeddings and add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 196)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Iterable of strings to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 199)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
**kwargs: `VectorStore` specific parameters.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 202)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
List of IDs from adding the texts into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 211)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if type(self).aadd_documents != VectorStore.aadd_documents:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 235)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Add or update documents in the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 238)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: Documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 247)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if type(self).add_texts != VectorStore.add_texts:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 268)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Async run more documents through the embeddings and add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 271)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: Documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 278)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if type(self).aadd_texts != VectorStore.aadd_texts:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 311)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return self.similarity_search(query, **kwargs)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 346)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return await self.asimilarity_search(query, **kwargs)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 361)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 380)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# - the distance / similarity metric used by the VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 408)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
- The distance / similarity metric used by the VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 606)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def asimilarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 793)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Return `VectorStore` initialized from documents and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 796)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: List of `Document` objects to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 801)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStore` initialized from documents and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 823)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Async return `VectorStore` initialized from documents and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 826)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: List of `Document` objects to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 831)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStore` initialized from documents and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 857)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Return `VectorStore` initialized from texts and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 860)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Texts to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 867)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStore` initialized from texts and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 880)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Async return `VectorStore` initialized from texts and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 883)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Texts to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 890)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStore` initialized from texts and embeddings.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 905)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def as_retriever(self, **kwargs: Any) -> VectorStoreRetriever:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 906)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Return `VectorStoreRetriever` initialized from this `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 942)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch.as_retriever(search_type="mmr", search_kwargs={"k": 5, "fetch_k": 50})
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 967)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 968)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""VectorStore to use for retrieval."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1045)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docs = self.vectorstore.similarity_search(query, **kwargs_)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1070)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docs = await self.vectorstore.asimilarity_search(query, **kwargs_)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1088)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Add documents to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1091)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: Documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1102)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Async add documents to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1105)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: Documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 17)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class InMemoryVectorStore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 53)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 56)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = InMemoryVectorStore(OpenAIEmbeddings())
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 135)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# results = vector_store.asimilarity_search(query="thud", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 149)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = vector_store.as_retriever(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 404)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 410)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def asimilarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 494)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 509)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 519)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 528)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
A `VectorStore` object.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/benchmarks/test_imports.py` (line 29)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"from langchain_core.vectorstores import InMemoryVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/benchmarks/test_imports.py` (line 30)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
id="InMemoryVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 12)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class DummyVectorStore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 39)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 71)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> "DummyVectorStore":
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 72)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = DummyVectorStore(**kwargs)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 79)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = DummyVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 89)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = DummyVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 99)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = DummyVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 108)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = DummyVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 122)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls=DummyVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 134)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(selector.vectorstore, DummyVectorStore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 148)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls=DummyVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 160)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(selector.vectorstore, DummyVectorStore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 169)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = DummyVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 182)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = DummyVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 200)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls=DummyVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 214)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(selector.vectorstore, DummyVectorStore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 228)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls=DummyVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/example_selectors/test_similarity.py` (line 242)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(selector.vectorstore, DummyVectorStore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 23)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import InMemoryVectorStore, VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 62)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vector_store() -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 65)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore(embeddings)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 69)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def upserting_vector_store() -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 72)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore(embeddings)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 76)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 110)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 154)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 263)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 370)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 471)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 572)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 798)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 924)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1109)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1194)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1284)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1374)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1487)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1569)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1649)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1846)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1999)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2029)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2059)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2106)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(vector_store, InMemoryVectorStore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2115)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2367)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2458)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, upserting_vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2518)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, upserting_vector_store: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2578)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2615)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2783)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, upserting_vector_store: InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2914)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, upserting_vector_store: InMemoryVectorStore
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/tests/unit_tests/language_models/chat_models/test_base.py` (line 972)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
response = llm.invoke("hello")
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/tests/unit_tests/language_models/chat_models/test_base.py` (line 977)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
response = llm.invoke("hello")
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 60)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"Secret was leaked in deserialized object! Found '{SENTINEL_VALUE}'.\n"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 69)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`HumanMessage` with secret-like dict in `content`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 79)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`HumanMessage` with secret-like dict in `additional_kwargs`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 87)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`HumanMessage` with secret-like dict nested in `additional_kwargs`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 95)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`HumanMessage` with secret-like dict in a list in `additional_kwargs`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 103)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`AIMessage` with secret-like dict in respo`nse_metadata."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 111)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Document with secret-like dict in `metadata`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 119)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`AIMessage` containing `dumpd(HumanMessage)` with secret in kwargs."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 135)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Dict containing a `Serializable` with secret-like dict."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 144)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Dict with secret-like dict, no `Serializable` objects."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 149)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Dict with nested secret-like dict, no `Serializable` objects."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 176)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Pydantic model containing a `Serializable` with secret-like dict."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 218)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Custom class containing a `Serializable` with secret-like dict."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 233)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Custom class containing a secret-like dict directly."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 253)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`AIMessage` with `dumpd(HumanMessage w/ secret)` in `additional_kwargs`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 290)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Verify secret-like dict in `Document` metadata is preserved."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 277)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"type": "text", "text": "This is the FIRST 4 token block."},
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 278)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"type": "text", "text": "This is the SECOND 4 token block."},
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 308)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
[{"type": "text", "text": "This is the FIRST 4 token block."}], id="second"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 363)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"type": "text", "text": "This is the SECOND 4 token block."},
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 389)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"type": "text", "text": "This is the SECOND 4 token block."},
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 711)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that invalid `token_counter` shortcut raises `ValueError`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 962)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
return "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgy
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2766)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test approximate token counting with image content blocks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2780)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert token_count < 200, f"Expected <200 tokens, got {token_count}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2781)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert token_count > 80, f"Expected >80 tokens, got {token_count}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2850)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that unknown multimodal block types still contribute to token count."""
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/tests/unit_tests/prompts/test_chat.py` (line 350)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
result = template.invoke({"name": "Alice", "question": "Hello?"})
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/core/tests/unit_tests/prompts/test_dict.py` (line 45)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
template={"output": "{message.additional_kwargs[secret]}"},
```

### [HIGH] Dangerous execution pattern: __import__ dynamic import
- **File:** `libs/core/tests/unit_tests/prompts/test_loading.py` (line 331)
- **Category:** dynamic_import
- **OWASP:** LLM07 — Insecure Plugin Design

```
".__import__('os').popen('id').read() }}"
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/core/tests/unit_tests/runnables/test_tracing_interops.py` (line 615)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
return chain.invoke(x, config={"callbacks": [tracer]})
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 13)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestInMemoryStandard(VectorStoreIntegrationTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore(embedding=self.get_embeddings())
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 19)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_inmemory_similarity_search() -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 21)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = await InMemoryVectorStore.afrom_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 26)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = store.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 30)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await store.asimilarity_search("bar", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 39)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = await InMemoryVectorStore.afrom_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 52)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore = InMemoryVectorStore(embedding=DeterministicFakeEmbedding(size=6))
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 68)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = await InMemoryVectorStore.afrom_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 89)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = InMemoryVectorStore.from_texts(["foo", "bar", "baz"], embedding)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 90)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = store.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 184)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = InMemoryVectorStore(embedding=DeterministicFakeEmbedding(size=3))
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 215)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = InMemoryVectorStore(embedding=embeddings_mock)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 218)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
await store.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 17)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 23)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class CustomAddTextsVectorstore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""A VectorStore that only implements add texts."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 68)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 74)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class CustomAddDocumentsVectorstore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 75)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""A VectorStore that only implements add documents."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 114)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 123)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_default_add_documents(vs_class: type[VectorStore]) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 126)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
Test that we can implement the upsert method of the CustomVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 154)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_default_add_texts(vs_class: type[VectorStore]) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 184)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_default_aadd_documents(vs_class: type[VectorStore]) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 211)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_default_aadd_texts(vs_class: type[VectorStore]) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 242)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_default_from_documents(vs_class: type[VectorStore]) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/core/tests/unit_tests/vectorstores/test_vectorstore.py` (line 271)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_default_afrom_documents(vs_class: type[VectorStore]) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/__init__.py` (line 32)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreInfo,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/__init__.py` (line 33)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreRouterToolkit,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/__init__.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreToolkit,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/__init__.py` (line 153)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreInfo",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/__init__.py` (line 154)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreRouterToolkit",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/__init__.py` (line 155)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreToolkit",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 1)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""VectorStore agent."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreRouterToolkit,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreToolkit,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 33)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
toolkit: VectorStoreToolkit,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Construct a VectorStore agent from an LLM and tools.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 52)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 58)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = InMemoryVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 67)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store.as_retriever(),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 125)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
toolkit: VectorStoreRouterToolkit,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 132)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Construct a VectorStore router agent from an LLM and tools.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 144)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 150)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
pet_vector_store = InMemoryVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 158)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
food_vector_store = InMemoryVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 168)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
pet_vector_store.as_retriever(),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/base.py` (line 173)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
food_vector_store.as_retriever(),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 10)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreInfo(BaseModel):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Information about a `VectorStore`."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 13)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore = Field(exclude=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreToolkit(BaseToolkit):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 23)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Toolkit for interacting with a `VectorStore`."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 25)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_info: VectorStoreInfo = Field(exclude=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 36)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreQATool,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 37)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreQAWithSourcesTool,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 42)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
description = VectorStoreQATool.get_description(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 46)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_tool = VectorStoreQATool(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 52)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
description = VectorStoreQAWithSourcesTool.get_description(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 56)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_with_sources_tool = VectorStoreQAWithSourcesTool(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 65)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreRouterToolkit(BaseToolkit):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 68)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstores: list[VectorStoreInfo] = Field(exclude=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 80)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreQATool,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 86)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
description = VectorStoreQATool.get_description(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/agent_toolkits/vectorstore/toolkit.py` (line 90)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_tool = VectorStoreQATool(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/openai_assistant/base.py` (line 673)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
run = self.client.beta.threads.runs.retrieve(run_id, thread_id=thread_id)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/agents/openai_assistant/base.py` (line 826)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
run = await self.async_client.beta.threads.runs.retrieve(
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/langchain_classic/agents/openai_functions_agent/base.py` (line 125)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
predicted_message = self.llm.invoke(
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/langchain_classic/agents/openai_functions_agent/base.py` (line 131)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
predicted_message = self.llm.invoke(
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/langchain_classic/agents/openai_functions_multi_agent/base.py` (line 228)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
predicted_message = self.llm.invoke(
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/callbacks/streaming_stdout_final_only.py` (line 82)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Run on new LLM token. Only available when streaming is enabled."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/__init__.py` (line 30)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ConversationalRetrievalChain": (
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/__init__.py` (line 71)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RetrievalQAWithSourcesChain": "langchain_classic.chains.qa_with_sources.retrieval",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/__init__.py` (line 74)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RetrievalQA": "langchain_classic.chains.retrieval_qa.base",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/__init__.py` (line 78)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"MultiRetrievalQAChain": "langchain_classic.chains.router",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 69)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Input type for ConversationalRetrievalChain."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 77)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class BaseConversationalRetrievalChain(Chain):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 263)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class ConversationalRetrievalChain(BaseConversationalRetrievalChain):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 354)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ConversationalRetrievalChain,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 361)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = vectorstore.as_retriever()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 373)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
chain = ConversationalRetrievalChain(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 449)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> BaseConversationalRetrievalChain:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 471)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ConversationalRetrievalChain
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 498)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class ChatVectorDBChain(BaseConversationalRetrievalChain):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 501)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore = Field(alias="vectorstore")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 515)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ConversationalRetrievalChain`",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 531)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return self.vectorstore.similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 552)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 558)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> BaseConversationalRetrievalChain:
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 32)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Extract tokens and log probabilities from chat model response."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 115)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Minimum probability for a token to be considered low confidence."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 117)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Minimum number of tokens between two low confidence spans."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 119)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Number of tokens to pad around a low confidence span."""
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 145)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
docs.extend(self.retriever.invoke(question))
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 147)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
result = self.response_chain.invoke(
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 299)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"FlareChain.from_llm: supplied llm max_completion_tokens=%s "
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/langchain_classic/chains/llm.py` (line 61)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
chain.invoke("your adjective here")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/loading.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
RetrievalQAWithSourcesChain,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/loading.py` (line 39)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_classic.chains.retrieval_qa.base import RetrievalQA, VectorDBQA
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/loading.py` (line 462)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def _load_retrieval_qa(config: dict, **kwargs: Any) -> RetrievalQA:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/loading.py` (line 485)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return RetrievalQA(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/loading.py` (line 495)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> RetrievalQAWithSourcesChain:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/loading.py` (line 518)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return RetrievalQAWithSourcesChain(
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/chains/natbot/base.py` (line 82)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"model = OpenAI(temperature=0.5, best_of=10, n=3, max_tokens=50)"
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/retrieval.py` (line 17)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class RetrievalQAWithSourcesChain(BaseQAWithSourcesChain):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/vector_db.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/vector_db.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore = Field(exclude=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/vector_db.py` (line 60)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docs = self.vectorstore.similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/vector_db.py` (line 82)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RetrievalQAWithSourcesChain`",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 19)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class BaseRetrievalQA(Chain):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 77)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> BaseRetrievalQA:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 110)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> BaseRetrievalQA:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 218)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class RetrievalQA(BaseRetrievalQA):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 257)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_classic.chains import RetrievalQA
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 259)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStoreRetriever
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 261)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = VectorStoreRetriever(vectorstore=FAISS(...))
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 262)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retrievalQA = RetrievalQA.from_llm(llm=OpenAI(), retriever=retriever)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 307)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorDBQA(BaseRetrievalQA):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 310)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore = Field(exclude=True, alias="vectorstore")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 339)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docs = self.vectorstore.similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/__init__.py` (line 4)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_classic.chains.router.multi_retrieval_qa import MultiRetrievalQAChain
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/__init__.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"MultiRetrievalQAChain",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 12)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 42)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = self.vectorstore.similarity_search(_input, k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 52)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = await self.vectorstore.asimilarity_search(_input, k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 59)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 79)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/multi_retrieval_qa.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_classic.chains.retrieval_qa.base import BaseRetrievalQA, RetrievalQA
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/multi_retrieval_qa.py` (line 27)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class MultiRetrievalQAChain(MultiRouteChain):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/multi_retrieval_qa.py` (line 36)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
destination_chains: Mapping[str, BaseRetrievalQA]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/multi_retrieval_qa.py` (line 57)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> MultiRetrievalQAChain:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/multi_retrieval_qa.py` (line 96)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
chain = RetrievalQA.from_llm(llm, prompt=prompt, retriever=retriever)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/chains/router/multi_retrieval_qa.py` (line 102)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
_default_chain = RetrievalQA.from_llm(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 14)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
RetrievalQAWithSourcesChain,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreIndexWrapper(BaseModel):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 25)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Wrapper around a `VectorStore` for easy access."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 27)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 41)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Query the `VectorStore` using the provided LLM.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 50)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
The result string from the RetrievalQA chain.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 62)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
chain = RetrievalQA.from_chain_type(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 64)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever=self.vectorstore.as_retriever(**retriever_kwargs),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 76)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Asynchronously query the `VectorStore` using the provided LLM.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 85)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
The asynchronous result string from the RetrievalQA chain.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 97)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
chain = RetrievalQA.from_chain_type(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 99)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever=self.vectorstore.as_retriever(**retriever_kwargs),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 111)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Query the `VectorStore` and retrieve the answer along with sources.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 132)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
chain = RetrievalQAWithSourcesChain.from_chain_type(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 134)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever=self.vectorstore.as_retriever(**retriever_kwargs),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 146)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Asynchronously query the `VectorStore` and retrieve the answer and sources.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 167)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
chain = RetrievalQAWithSourcesChain.from_chain_type(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 169)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever=self.vectorstore.as_retriever(**retriever_kwargs),
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 175)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def _get_in_memory_vectorstore() -> type[VectorStore]:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 176)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Get the `InMemoryVectorStore`."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 180)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores.inmemory import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 182)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
msg = "Please install langchain-community to use the InMemoryVectorStore."
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 185)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"Using InMemoryVectorStore as the default vectorstore."
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 187)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"specify a VectorStore when using VectorstoreIndexCreator",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 190)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 196)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore_cls: type[VectorStore] = Field(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 208)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def from_loaders(self, loaders: list[BaseLoader]) -> VectorStoreIndexWrapper:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 209)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Create a `VectorStore` index from a list of loaders.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 215)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
A `VectorStoreIndexWrapper` containing the constructed vectorstore.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 222)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def afrom_loaders(self, loaders: list[BaseLoader]) -> VectorStoreIndexWrapper:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 223)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Asynchronously create a `VectorStore` index from a list of loaders.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 229)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
A `VectorStoreIndexWrapper` containing the constructed vectorstore.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 236)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def from_documents(self, documents: list[Document]) -> VectorStoreIndexWrapper:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 237)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Create a `VectorStore` index from a list of documents.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 243)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
A `VectorStoreIndexWrapper` containing the constructed vectorstore.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 251)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return VectorStoreIndexWrapper(vectorstore=vectorstore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 256)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> VectorStoreIndexWrapper:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 257)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Asynchronously create a `VectorStore` index from a list of documents.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 263)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
A `VectorStoreIndexWrapper` containing the constructed vectorstore.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 271)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return VectorStoreIndexWrapper(vectorstore=vectorstore)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/__init__.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_classic.memory.vectorstore import VectorStoreRetrieverMemory
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/__init__.py` (line 26)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ConversationVectorStoreTokenBufferMemory,  # avoid circular import
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/__init__.py` (line 102)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ConversationVectorStoreTokenBufferMemory",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/__init__.py` (line 122)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreRetrieverMemory",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/langchain_classic/memory/summary_buffer.py` (line 130)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Asynchronously prune buffer if it exceeds max token limit."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore.py` (line 1)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Class for a VectorStore-backed memory object."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore.py` (line 8)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStoreRetriever
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore.py` (line 26)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreRetrieverMemory(BaseMemory):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore.py` (line 33)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever: VectorStoreRetriever = Field(exclude=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""VectorStoreRetriever object to connect to."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
saved to a `VectorStore` backing database. The `VectorStore` can be made persistent
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStoreRetriever
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 20)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreRetrieverMemory,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 37)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class ConversationVectorStoreTokenBufferMemory(ConversationTokenBufferMemory):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 55)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever: (required) A VectorStoreRetriever object to use
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 69)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ConversationVectorStoreTokenBufferMemory,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 84)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = chroma.as_retriever(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 92)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
conversation_memory = ConversationVectorStoreTokenBufferMemory(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 107)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever: VectorStoreRetriever = Field(exclude=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 112)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
_memory_retriever: VectorStoreRetrieverMemory | None = PrivateAttr(default=None)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 116)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def memory_retriever(self) -> VectorStoreRetrieverMemory:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 160)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
Useful if you have made the VectorStore persistent, in which
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/__init__.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/__init__.py` (line 162)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"TimeWeightedVectorStoreRetriever",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 45)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 46)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""The underlying `VectorStore` to use to store small chunks
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 105)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
sub_docs = self.vectorstore.similarity_search(query, **self.search_kwargs)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 144)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
sub_docs = await self.vectorstore.asimilarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/parent_document_retriever.py` (line 47)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# The VectorStore to use to index the child chunks
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/parent_document_retriever.py` (line 136)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
**kwargs: additional keyword arguments passed to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/parent_document_retriever.py` (line 167)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
**kwargs: additional keyword arguments passed to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 29)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def _get_builtin_translator(vectorstore: VectorStore) -> Visitor:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 84)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
SupabaseVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 103)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
builtin_translators: dict[type[VectorStore], type[Visitor]] = {
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 117)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
SupabaseVectorStore: SupabaseVectorTranslator,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 137)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_astradb.vectorstores import AstraDBVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 141)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(vectorstore, AstraDBVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 153)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_pinecone import PineconeVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 157)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(vectorstore, PineconeVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 203)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 207)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(vectorstore, QdrantVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 222)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_weaviate.vectorstores import WeaviateVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 227)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(vectorstore, WeaviateVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 243)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 254)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Translator for turning internal query language into `VectorStore` search params."""  # noqa: E501
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 300)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return self.vectorstore.search(query, self.search_type, **search_kwargs)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 345)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/self_query/base.py` (line 363)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
language into `VectorStore` search params.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/time_weighted_retriever.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/time_weighted_retriever.py` (line 21)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TimeWeightedVectorStoreRetriever(BaseRetriever):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/time_weighted_retriever.py` (line 27)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/time_weighted_retriever.py` (line 28)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""The `VectorStore` to store documents and determine salience."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/retrievers/time_weighted_retriever.py` (line 31)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Keyword arguments to pass to the `VectorStore` similarity search."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/schema/vectorstore.py` (line 1)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VST, VectorStore, VectorStoreRetriever
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/schema/vectorstore.py` (line 3)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
__all__ = ["VST", "VectorStore", "VectorStoreRetriever"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/__init__.py` (line 184)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQATool",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/__init__.py` (line 185)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQAWithSourcesTool",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/vectorstore/tool.py` (line 7)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreQATool,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/vectorstore/tool.py` (line 8)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStoreQAWithSourcesTool,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/vectorstore/tool.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQATool": "langchain_community.tools",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/vectorstore/tool.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQAWithSourcesTool": "langchain_community.tools",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/vectorstore/tool.py` (line 28)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQATool",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/tools/vectorstore/tool.py` (line 29)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQAWithSourcesTool",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 10)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 39)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
EcloudESVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 56)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
NeuralDBClientVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 57)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
NeuralDBVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 68)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
SKLearnVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 71)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
SupabaseVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 84)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ZepVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 114)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"EcloudESVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 132)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NeuralDBClientVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 133)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NeuralDBVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 134)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NEuralDBVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 145)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 148)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SupabaseVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 161)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ZepVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 197)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"EcloudESVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 214)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NeuralDBClientVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 215)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NeuralDBVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 223)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 229)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SupabaseVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 239)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/__init__.py` (line 243)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ZepVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/azuresearch.py` (line 8)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
AzureSearchVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/azuresearch.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"AzureSearchVectorStoreRetriever": "langchain_community.vectorstores.azuresearch",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/azuresearch.py` (line 29)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"AzureSearchVectorStoreRetriever",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/baiducloud_vector_search.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores import BESVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/baiducloud_vector_search.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
DEPRECATED_LOOKUP = {"BESVectorStore": "langchain_community.vectorstores"}
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/baiducloud_vector_search.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"BESVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/base.py` (line 1)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/base.py` (line 3)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
__all__ = ["VectorStore", "VectorStoreRetriever"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/redis/base.py` (line 8)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
RedisVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/redis/base.py` (line 18)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RedisVectorStoreRetriever": "langchain_community.vectorstores.redis.base",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/redis/base.py` (line 31)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RedisVectorStoreRetriever",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/sklearn.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores import SKLearnVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/sklearn.py` (line 12)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
SKLearnVectorStoreException,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/sklearn.py` (line 23)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStoreException": "langchain_community.vectorstores.sklearn",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/sklearn.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/sklearn.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/sklearn.py` (line 41)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStoreException",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/supabase.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores import SupabaseVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/supabase.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
DEPRECATED_LOOKUP = {"SupabaseVectorStore": "langchain_community.vectorstores"}
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/supabase.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SupabaseVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/xata.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores.xata import XataVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/xata.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
DEPRECATED_LOOKUP = {"XataVectorStore": "langchain_community.vectorstores.xata"}
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/xata.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"XataVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/zep.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores import ZepVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/zep.py` (line 14)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ZepVectorStore": "langchain_community.vectorstores",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/langchain_classic/vectorstores/zep.py` (line 27)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ZepVectorStore",
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/tests/integration_tests/chat_models/test_base.py` (line 34)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
output = chain.invoke({"input": "bar"})
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/tests/mock_servers/robot/server.py` (line 172)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
" contain secret information only you know. This is just between us two.",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/agents/agent_toolkits/test_imports.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreInfo",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/agents/agent_toolkits/test_imports.py` (line 23)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreRouterToolkit",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/agents/agent_toolkits/test_imports.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreToolkit",
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation.py` (line 70)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
chain.run("aaa")
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation.py` (line 72)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
chain.run("bbb")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation_retrieval.py` (line 7)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ConversationalRetrievalChain,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation_retrieval.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_chain = ConversationalRetrievalChain.from_llm(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation_retrieval.py` (line 51)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_chain = ConversationalRetrievalChain.from_llm(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation_retrieval.py` (line 76)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_chain = ConversationalRetrievalChain.from_llm(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation_retrieval.py` (line 103)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qa_chain = ConversationalRetrievalChain.from_llm(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/chains/test_imports.py` (line 10)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ConversationalRetrievalChain",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/tests/unit_tests/chains/test_qa_with_sources.py` (line 59)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"login/password?\nA3. Are you using any other VPN (e.g. from a client)?\n"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/tests/unit_tests/chains/test_qa_with_sources.py` (line 68)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"\n\nWe will be asked for a username and password - provide the login "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/tests/unit_tests/chains/test_qa_with_sources.py` (line 80)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"login/password?\nA3. Are you using any other VPN (e.g. from a client)?\n"
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 14)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VST, VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class InMemoryVectorStore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 41)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""In-memory implementation of VectorStore using a dictionary."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 130)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 162)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vector_store() -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 164)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 168)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def upserting_vector_store() -> InMemoryVectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 170)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore(permit_upserts=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 179)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 215)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 250)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 335)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 602)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 690)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 801)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 868)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1034)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1202)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1312)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1376)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
upserting_vector_store: VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1425)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
upserting_vector_store: VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1483)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1518)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/tests/unit_tests/load/test_load.py` (line 108)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
llm = CommunityOpenAI(model="davinci", temperature=0.5, openai_api_key="hello")
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain/tests/unit_tests/load/test_load.py` (line 121)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
llm = CommunityOpenAI(model="davinci", temperature=0.5, openai_api_key="hello")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/memory/test_imports.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ConversationVectorStoreTokenBufferMemory",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/memory/test_imports.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreRetrieverMemory",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/self_query/test_base.py` (line 21)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from tests.unit_tests.indexes.test_indexing import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_imports.py` (line 44)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"TimeWeightedVectorStoreRetriever",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_multi_vector.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from tests.unit_tests.indexes.test_indexing import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_multi_vector.py` (line 12)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class InMemoryVectorstoreWithSearch(InMemoryVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_multi_vector.py` (line 21)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_parent_document.py` (line 10)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from tests.unit_tests.indexes.test_indexing import InMemoryVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_parent_document.py` (line 13)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class InMemoryVectorstoreWithSearch(InMemoryVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_parent_document.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 10)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 14)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 32)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class MockVectorStore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 45)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 56)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type["MockVectorStore"],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 61)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> "MockVectorStore":
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 83)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def time_weighted_retriever() -> TimeWeightedVectorStoreRetriever:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 84)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore = MockVectorStore()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 85)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return TimeWeightedVectorStoreRetriever(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 100)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 121)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 133)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 145)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 163)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 181)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/retrievers/test_time_weighted_retriever.py` (line 194)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
time_weighted_retriever: TimeWeightedVectorStoreRetriever,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/schema/test_vectorstore.py` (line 3)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
EXPECTED_ALL = ["VectorStore", "VectorStoreRetriever", "VST"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/tools/test_imports.py` (line 111)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQATool",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/tools/test_imports.py` (line 112)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreQAWithSourcesTool",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 28)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"EcloudESVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 46)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NeuralDBClientVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 47)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"NeuralDBVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 58)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SKLearnVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 61)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"SupabaseVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 71)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/langchain/tests/unit_tests/vectorstores/test_public_api.py` (line 75)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"ZepVectorStore",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/context_editing.py` (line 59)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Configuration for clearing tool outputs when token limits are exceeded."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/context_editing.py` (line 65)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Minimum number of tokens to reclaim when the edit runs."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/shell_tool.py` (line 61)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"confirm the working directory is correct (e.g., inspect with `ls` or `pwd`) and ensure "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 209)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Tune parameters of approximate token counter based on model type."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 309)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"max_tokens_before_summary is deprecated. Use trigger=('tokens', value) instead.",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 362)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"and is unavailable for the specified model. Please use absolute token "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 364)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
'`\n\nChatModel(..., profile={"max_input_tokens": ...})`.\n\n'
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 564)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Check if reported token usage from last AIMessage exceeds threshold."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 584)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Determine whether summarization should run for the current token usage."""
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/langchain_v1/tests/integration_tests/chat_models/test_base.py` (line 32)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
output = chain.invoke({"input": "bar"})
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 246)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
with pytest.warns(DeprecationWarning, match="max_tokens_before_summary is deprecated"):
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 376)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Ensure token retention preserves AI/Tool message pairs together."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 760)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test binary search in _find_token_based_cutoff with edge cases."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 889)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test handling of edge cases with target token calculations."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 995)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
with pytest.warns(DeprecationWarning, match="max_tokens_before_summary is deprecated"):
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1079)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"langchain.agents.middleware.summarization.count_tokens_approximately",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1692)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""A clause combining `tokens` and `fraction` (no `messages`) is AND-evaluated."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1753)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"get_buffer_string should produce fewer tokens than count_tokens_approximately. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1761)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"str(messages) should produce significantly more tokens. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1994)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Fraction triggers should account for provider-reported token usage."""
```

### [HIGH] Dangerous execution pattern: eval() with non-literal argument
- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_tool_emulator.py` (line 40)
- **Category:** eval_usage
- **OWASP:** LLM07 — Insecure Plugin Design

```
return f"Result: {eval(expression)}"  # noqa: S307
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/langchain_v1/tests/unit_tests/agents/test_create_agent_tool_validation.py` (line 410)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Error should NOT contain password value (from system-injected state)"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 931)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Number of most likely tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 934)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Total probability mass of tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 963)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Automatically read from env var `ANTHROPIC_API_KEY` if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 1096)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return a mapping of secret keys to environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 1155)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Set default `max_tokens` from model profile with fallback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 1873)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
#     response_metadata={'id': 'msg_01GM3zQtoFv8jGQMW7abLnhi', 'model': 'claude-sonnet-4-5-20250929', 'stop_reason': 'to
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 40)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Number of most likely tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 43)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Total probability mass of tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 72)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Automatically read from env var `ANTHROPIC_API_KEY` if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 161)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return a mapping of secret keys to environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 418)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"ChatAnthropic.get_num_tokens_from_messages instead."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 51)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from Anthropic."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 97)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from Anthropic."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 375)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 391)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 433)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from Anthropic."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 449)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from Anthropic."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_llms.py` (line 46)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/integration_tests/test_llms.py` (line 67)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/unit_tests/test_chat_models.py` (line 139)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test the set_default_max_tokens function."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/unit_tests/test_chat_models.py` (line 2917)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
message="prompt is too long: 209752 tokens > 200000 maximum",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/anthropic/tests/unit_tests/test_chat_models.py` (line 2923)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"message": "prompt is too long: 209752 tokens > 200000 maximum",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 26)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 155)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class Chroma(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 274)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# results = vector_store.asimilarity_search(query="thud",k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 288)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = vector_store.as_retriever(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 1414)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents: List of documents to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 49)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 65)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 83)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 99)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await docsearch.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 117)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await docsearch.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 135)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 155)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 298)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 345)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 457)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search(updated_content, k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 518)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search(updated_content, k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 586)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
search = db.similarity_search("foo bar")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 792)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore.similarity_search("foo")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/unit_tests/test_standard.py` (line 4)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/unit_tests/test_standard.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/unit_tests/test_standard.py` (line 11)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestChromaStandard(VectorStoreIntegrationTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/unit_tests/test_standard.py` (line 13)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore[override]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/unit_tests/test_vectorstores.py` (line 18)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_similarity_search() -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/chroma/tests/unit_tests/test_vectorstores.py` (line 28)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/deepseek/langchain_deepseek/chat_models.py` (line 244)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "If using default api base, DEEPSEEK_API_KEY must be set."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/exa/langchain_exa/tools.py` (line 79)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
content="Title: San Francisco, CA Weather Conditionsstar_ratehome\nURL: https://www.wunderground.com/weather/37.8,-122.4
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/langchain_fireworks/chat_models.py` (line 744)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"You can pass it an argument as `api_key=...` or "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/langchain_fireworks/chat_models.py` (line 745)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"set the environment variable `FIREWORKS_API_KEY`."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/langchain_fireworks/embeddings.py` (line 76)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"You can pass it an argument as `api_key=...` or "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/langchain_fireworks/embeddings.py` (line 77)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"set the environment variable `FIREWORKS_API_KEY`."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/langchain_fireworks/llms.py` (line 48)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"You can pass it an argument as `api_key=...` or "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/langchain_fireworks/llms.py` (line 49)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"set the environment variable `FIREWORKS_API_KEY`."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 64)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from ChatFireworks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 84)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Expected exactly one chunk with token counts or response_metadata. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 103)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from ChatFireworks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 114)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test invoke tokens from ChatFireworks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 122)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test invoke tokens from ChatFireworks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 49)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 57)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 74)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from Fireworks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 85)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from Fireworks."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/fireworks/tests/unit_tests/test_chat_models.py` (line 1061)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""When provider omits total_tokens, sum input + output."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/langchain_groq/chat_models.py` (line 400)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
alias="api_key", default_factory=secret_from_env("GROQ_API_KEY", default=None)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/langchain_groq/chat_models.py` (line 402)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Automatically inferred from env var `GROQ_API_KEY` if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/langchain_groq/chat_models.py` (line 564)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Mapping of secret environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 60)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test ainvoke tokens from ChatGroq."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 70)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from ChatGroq."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 81)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test abatch tokens from ChatGroq."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 120)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Expected exactly one chunk with token counts or metadata. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 183)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 200)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 308)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
llm = ChatGroq(model="foo", api_key=secret, model_kwargs={"not_secret": not_secret})  # type: ignore[call-arg, arg-type]
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 464)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that explicit total_tokens=0 is preserved, not replaced by sum."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 477)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that input_tokens=0 is not overridden by prompt_tokens fallback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 491)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that output_tokens=0 is not overridden by completion_tokens fallback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 523)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that zero cached tokens are not included (falsy)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 587)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that zero reasoning tokens are not included (falsy)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 667)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that _create_chat_result properly includes reasoning tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 713)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that _create_chat_result includes both cached and reasoning tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 846)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming properly includes reasoning tokens in usage metadata."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 962)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that _combine_llm_outputs properly combines nested token details."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 496)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Tokenizer for the model. Only used for HuggingFacePipeline."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 506)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Penalizes repeated tokens according to frequency."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 516)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Modify the likelihood of specified tokens appearing in the completion."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 525)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Total probability mass of tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 1033)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Make sure that your Hugging Face token has access to the endpoint."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/langchain_huggingface/llms/huggingface_endpoint.py` (line 143)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Stop generating tokens if a member of `stop_sequences` is generated"""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/tests/integration_tests/test_llms.py` (line 7)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from huggingface_pipeline."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/tests/unit_tests/test_chat_models.py` (line 236)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that _default_params includes inherited max_tokens from max_new_tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/huggingface/tests/unit_tests/test_huggingface_endpoint.py` (line 67)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""HF-hosted endpoint_url still gets the token."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 52)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Dummy tokenizer for when tokenizer cannot be accessed (e.g., via Huggingface)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 210)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Could not download mistral tokenizer from Huggingface for "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 211)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"calculating batch sizes. Set a Huggingface token via the "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 212)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"HF_TOKEN environment variable to download the real tokenizer. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 213)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Falling back to a dummy tokenizer that uses `len()`.",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 220)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Split list of texts into batches of less than 16k tokens for Mistral API."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/tests/integration_tests/test_chat_models.py` (line 20)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from ChatMistralAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/tests/integration_tests/test_chat_models.py` (line 38)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Expected exactly one chunk with token counts or response_metadata. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/mistralai/tests/unit_tests/test_embeddings.py` (line 77)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that DummyTokenizer returns character lists."""
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 19)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
result = llm.invoke("I'm Pickle Rick", config=RunnableConfig(tags=["foo"]))
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 32)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch sync token generation from `OllamaLLM`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 41)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch async token generation from `OllamaLLM`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 72)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming raw string tokens from `OllamaLLM`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 80)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test async streaming raw string tokens from `OllamaLLM`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 1)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URL authentication parsing functionality."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 15)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test the parse_url_with_auth utility function."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 23)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URLs without authentication credentials."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 36)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URLs with authentication credentials."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 37)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url = "https://user:password@ollama.example.com:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 62)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test scheme-less URL with authentication credentials."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 63)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url = "user:password@ollama.example.com:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 74)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URLs with auth, path, and query parameters."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 99)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URLs with only username (no password)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 111)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URLs with empty password."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 124)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URL authentication integration with ChatOllama."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 131)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that ChatOllama properly handles URL authentication."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 132)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url_with_auth = "https://user:password@ollama.example.com:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 155)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url_with_auth = "https://user:password@ollama.example.com:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 179)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URL authentication integration with OllamaLLM."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 186)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that OllamaLLM properly handles URL authentication."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 187)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url_with_auth = "https://user:password@ollama.example.com:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 205)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test URL authentication integration with OllamaEmbeddings."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 212)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that OllamaEmbeddings properly handles URL authentication."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 213)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url_with_auth = "https://user:password@ollama.example.com:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 242)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url = "https://user:password@ollama.example.com"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 279)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
url = "https://user:password@[::1]:11434"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 297)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test with complex passwords containing special characters."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/azure.py` (line 495)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Automatically inferred from env var `AZURE_OPENAI_API_KEY` if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/azure.py` (line 588)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Get the mapping of secret environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 495)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"{type(new_usage)} and {type(overall_token_usage)}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 503)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"{type(new_usage)} and {type(overall_token_usage)}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 510)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
warnings.warn(f"Unexpected type for token usage: {type(new_usage)}")
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 525)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
or "Input tokens exceed the configured limit" in e.message
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 613)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 718)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Penalizes repeated tokens according to frequency."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 734)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Modify the likelihood of specified tokens appearing in the completion."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 743)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Total probability mass of tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 2097)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"get_num_tokens_from_messages() is not presently implemented "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 2099)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"https://platform.openai.com/docs/guides/text-generation/managing-tokens"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 3322)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Mapping of secret environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 69)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"subscription OAuth against Codex endpoints and must only be used where "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 386)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"`_ChatGPTOAuthTokenProvider` protocol."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 400)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"`_ChatOpenAICodex` manages authentication via "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 401)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"`token_provider`; drop the explicit `{key}=`. Use "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 402)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"`ChatOpenAI` if you want API-key authentication."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 536)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`_ChatOpenAICodex` is not serializable (holds a live token provider)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 61)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
CHATGPT_DEVICE_REDIRECT_URI = "https://auth.openai.com/deviceauth/callback"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 95)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Validate non-empty secrets and timezone-aware `expires_at`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 97)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "`access_token` must be a non-empty string."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 100)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "`refresh_token` must be a non-empty string."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 107)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return `True` if the token is past (or within `skew` of) expiry."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 122)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Refresh-aware token source consumed by `_ChatOpenAICodex`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 137)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return only the access token string (sync callable for SDKs)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 141)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return only the access token string (async callable for SDKs)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 175)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Pull the ChatGPT account/plan/user IDs out of an ID-token JWT."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 195)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"id_token; the `ChatGPT-Account-Id` header will be omitted."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 205)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = f"OAuth token response had invalid `expires_in`: {raw!r}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 209)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"OAuth token response had missing or non-positive `expires_in`; "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 210)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"refusing to store an immediately-expired token."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 221)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Build a `_ChatGPTToken` from an OAuth token-endpoint response."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 223)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "OAuth token response did not include an `access_token`."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 231)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"prior refresh token was available; re-run `login_chatgpt()`."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 336)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"fcntl is unavailable on this platform; ChatGPT token store "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 370)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return `(error_code, body_excerpt)` from an OAuth error response."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 389)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"ChatGPT refresh token is no longer valid (`invalid_grant`). "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 390)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Re-run `login_chatgpt()` to obtain a new token."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 393)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = f"OAuth request to {url} failed with status {resp.status_code}: {excerpt}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 506)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"Failed to read ChatGPT token store at {self.path}: {exc}. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 515)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"ChatGPT token store at {self.path} is not valid JSON: "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 523)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"ChatGPT token store at {self.path} is missing required "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 555)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Refreshing ChatGPT access token (refresh_token=%s).",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 569)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"No ChatGPT OAuth token found at {self.path}. Run "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 570)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"`langchain_openai.chatgpt_oauth.login_chatgpt()` first."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 632)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Return only the access-token string (async)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 667)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
return f"{CHATGPT_AUTHORIZE_URL}?{urllib.parse.urlencode(params)}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 701)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"ChatGPT OAuth callback returned error %r (%s)",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 801)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"Could not bind ChatGPT OAuth callback server on "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 817)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = f"Timed out waiting for ChatGPT OAuth callback on http://{host}:{port}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 844)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"`host={host!r}` is not a loopback address. The OAuth callback "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 911)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f"\nChatGPT sign-in: open the following URL in a browser:\n  {authorize_url}\n"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 913)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
logger.info("Opening ChatGPT sign-in flow at %s", CHATGPT_AUTHORIZE_URL)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 930)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "ChatGPT OAuth callback state mismatch."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 934)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = f"ChatGPT OAuth callback returned error: {result['error']} {description}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 938)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "ChatGPT OAuth callback did not include an authorization code."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 1031)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = f"Device authorization failed: {error}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 1035)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "Timed out waiting for ChatGPT device authorization."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/embeddings/azure.py` (line 125)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Automatically inferred from env var `AZURE_OPENAI_API_KEY` if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/embeddings/base.py` (line 23)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""API limit per request for embedding tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/embeddings/base.py` (line 238)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/azure.py` (line 110)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Mapping of secret keys to environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 188)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Total probability mass of tokens to consider at each step."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 191)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Penalizes repeated tokens according to frequency."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 206)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 208)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Automatically inferred from env var `OPENAI_API_KEY` if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 246)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Adjust the probability of specific tokens being generated."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 601)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "max_tokens set to -1 not supported for multiple inputs."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 681)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"(e.g. `ChatOpenAI(model=...).profile['max_input_tokens']`)"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 746)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Profile for model %s is missing `max_input_tokens`; "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 757)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"name, or read `max_input_tokens` from the model profile directly. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 903)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Mapping of secret keys to environment variables."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/conftest.py` (line 60)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Redact OAuth secret fields in a urlencoded form body."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/conftest.py` (line 148)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Scrubbed a JWT-shaped token from a non-UTF-8 response body "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/conftest.py` (line 80)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Stub `_FileChatGPTOAuthTokenProvider` token reads for Codex VCR tests."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 86)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 140)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 165)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 176)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 188)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 197)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from AzureChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 208)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from AzureChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 217)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test invoke tokens from AzureChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 226)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test invoke tokens from AzureChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 163)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 219)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 227)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from ChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 239)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test invoke tokens from ChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 272)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 329)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 421)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from ChatOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 56)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 70)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 77)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 84)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 94)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 102)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 109)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from AzureOpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 150)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 173)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 14)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 22)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 30)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 39)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 50)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test batch tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 103)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 115)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 124)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 133)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 145)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 155)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 164)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test streaming tokens from OpenAI."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 208)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 233)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_azure.py` (line 239)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that max_completion_tokens can be used as a direct parameter."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_azure.py` (line 257)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that max_tokens is converted to max_completion_tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 536)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
{"id":"chatcmpl-9nhARrdUiJWEMd5plwV1Gc9NCjb9M","object":"chat.completion.chunk","created":1721631035,"model":"gpt-5.5","
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 1116)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that explicit total_tokens=0 is preserved, not replaced by sum."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3932)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Input tokens exceed the configured limit of 272000 tokens. Your messages "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3933)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"resulted in 300007 tokens. Please reduce the length of the messages."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3966)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "Input tokens exceed the configured limit" in str(exc_info.value)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3980)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "Input tokens exceed the configured limit" in str(exc_info.value)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3994)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "Input tokens exceed the configured limit" in str(exc_info.value)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 4010)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "Input tokens exceed the configured limit" in str(exc_info.value)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 4024)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "Input tokens exceed the configured limit" in str(exc_info.value)
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 4053)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "Input tokens exceed the configured limit" in str(exc_info.value)
```

### [HIGH] Dangerous execution pattern: __import__ dynamic import
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_client_utils.py` (line 38)
- **Category:** dynamic_import
- **OWASP:** LLM07 — Insecure Plugin Design

```
__import__("sys").platform != "linux",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 29)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Minimal `_ChatGPTOAuthTokenProvider` for tests."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 110)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""The SDK-facing `api_key` must resolve to the provider's current token."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 569)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""The `api_key` callable wired into the SDK must yield the access token."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/embeddings/test_base.py` (line 104)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that embeddings respect the 300k token per request limit."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 1)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Unit tests for `langchain_openai.chatgpt_oauth`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 274)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
assert "redirect_uri=http%3A%2F%2Flocalhost%3A1455%2Fauth%2Fcallback" in url
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 419)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "ChatGPT refresh token is no longer valid (`invalid_grant`)."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 558)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""End-to-end happy path using a stubbed callback + token endpoint."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 834)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
path="/auth/callback?code=abc&state=xyz",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 846)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
path="/auth/callback?error=access_denied&error_description=nope",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 853)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
path="/auth/callback?code=abc&state=xyz",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 865)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
path="/auth/callback?error=access_denied&error_description=user+declined",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 879)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
path="/auth/callback?error=invalid_scope",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 891)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"/auth/callback?error=oops&error_description="
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 910)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
path="/auth/callback?error=access_denied&error_description=nope",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_load.py` (line 12)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
llm = OpenAI(model="davinci", temperature=0.5, openai_api_key="hello", top_p=0.8)  # type: ignore[call-arg]
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openai/tests/unit_tests/test_load.py` (line 27)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
llm = OpenAI(model="davinci", temperature=0.5, openai_api_key="hello")  # type: ignore[call-arg]
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/langchain_openrouter/chat_models.py` (line 229)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Maximum number of completion tokens to generate."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/langchain_openrouter/chat_models.py` (line 424)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "OPENROUTER_API_KEY must be set."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 215)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that API key is read from OPENROUTER_API_KEY env var."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 224)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
with pytest.raises(ValueError, match="OPENROUTER_API_KEY must be set"):
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 260)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that ls_max_tokens is set when max_tokens is configured."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 1879)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that explicit total_tokens=0 is preserved, not replaced by sum."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 1891)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""prompt_tokens=0 must not fall through to input_tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 1902)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""completion_tokens=0 must not fall through to output_tokens."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2110)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that total_tokens is computed if not provided."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2147)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that zero-value token details are preserved (not dropped)."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2163)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test fallback to input_tokens/output_tokens key names."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2470)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that max_completion_tokens is included when set."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 91)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Perplexity API key. Reads from `PPLX_API_KEY` or `PERPLEXITY_API_KEY`."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 111)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"Perplexity API key not provided. Pass `pplx_api_key` (or "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 112)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"`api_key`) to PerplexityEmbeddings, or set the `PPLX_API_KEY` "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 113)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"or `PERPLEXITY_API_KEY` environment variable."
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/partners/perplexity/tests/integration_tests/test_chat_models.py` (line 17)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
response = chat.invoke([message])
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/partners/perplexity/tests/integration_tests/test_search_api.py` (line 16)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
docs = retriever.invoke("What is the capital of France?")
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/perplexity/tests/unit_tests/test_chat_models.py` (line 163)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test _create_usage_metadata with basic token counts."""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/perplexity/tests/unit_tests/test_embeddings.py` (line 45)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""`api_key=` should be accepted via populate_by_name alias."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/__init__.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant.qdrant import QdrantVectorStore, RetrievalMode
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/__init__.py` (line 12)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"QdrantVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 15)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class QdrantVectorStoreError(Exception):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 25)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""`QdrantVectorStore` related exceptions."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 36)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class QdrantVectorStore(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 62)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 74)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store = QdrantVectorStore(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 102)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = vector_store.similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 170)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# results = vector_store.asimilarity_search(query="thud",k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 184)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = vector_store.as_retriever(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 340)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 503)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Add texts with embeddings to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 506)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
List of ids from adding the texts into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 878)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = self.client.retrieve(self.collection_name, ids, with_payload=True)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 892)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1008)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
- The distance / similarity metric used by the VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1201)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
raise QdrantVectorStoreError(msg)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1216)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
raise QdrantVectorStoreError(msg)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1238)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
raise QdrantVectorStoreError(msg)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 59)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
@deprecated(since="0.1.2", alternative="QdrantVectorStore", removal="0.5.0")
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 60)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class Qdrant(VectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 154)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Run more texts through the embeddings and add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 157)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Iterable of strings to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 168)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
List of ids from adding the texts into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 191)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Run more texts through the embeddings and add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 194)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Iterable of strings to add to the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 205)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
List of ids from adding the texts into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 1954)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
- The distance / similarity metric used by the VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/async_api/test_from_texts.py` (line 265)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await docsearch.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/async_api/test_similarity_search.py` (line 20)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_qdrant_similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/async_api/test_similarity_search.py` (line 38)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await docsearch.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_add_texts.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore, RetrievalMode
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_add_texts.py` (line 32)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_add_texts.py` (line 44)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foobar", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_add_texts.py` (line 63)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_add_texts.py` (line 94)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_add_texts.py` (line 127)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_existing.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant.qdrant import QdrantVectorStore, RetrievalMode
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_existing.py` (line 25)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test if the QdrantVectorStore.from_existing_collection reuses the collection."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_existing.py` (line 28)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_existing.py` (line 39)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
qdrant = QdrantVectorStore.from_existing_collection(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore, RetrievalMode
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 10)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant.qdrant import QdrantVectorStoreError
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 25)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 57)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 71)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
stored_ids = [point.id for point in vec_store.client.retrieve(collection_name, ids)]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 89)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 129)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 141)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 165)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 175)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
with pytest.raises(QdrantVectorStoreError) as excinfo:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 176)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 209)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 219)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
with pytest.raises(QdrantVectorStoreError) as excinfo:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 220)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 242)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 253)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
with pytest.raises(QdrantVectorStoreError) as excinfo:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 254)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 282)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 293)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 309)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
@pytest.mark.parametrize("content_payload_key", [QdrantVectorStore.CONTENT_KEY, "foo"])
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 311)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "bar"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 329)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 341)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("fabrin", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_from_texts.py` (line 363)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vec_store = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore, RetrievalMode
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant.qdrant import QdrantVectorStoreError
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 19)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"content_payload_key", [QdrantVectorStore.CONTENT_KEY, "test_content"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "test_metadata"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 47)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 82)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"content_payload_key", [QdrantVectorStore.CONTENT_KEY, "test_content"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 85)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "test_metadata"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 99)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_mmr.py` (line 112)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
with pytest.raises(QdrantVectorStoreError) as excinfo:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore, RetrievalMode
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 18)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 26)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 35)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
@pytest.mark.parametrize("content_payload_key", [QdrantVectorStore.CONTENT_KEY, "foo"])
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 42)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "bar"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 55)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 70)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
@pytest.mark.parametrize("content_payload_key", [QdrantVectorStore.CONTENT_KEY, "foo"])
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 72)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "bar"]
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 85)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 160)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 188)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 272)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 319)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 338)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 351)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test that as_retriever() works in SPARSE mode."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 354)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 371)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# Test basic as_retriever() functionality
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 372)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = vectorstore.as_retriever()
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 382)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert "QdrantVectorStore" in retriever.tags
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 387)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test as_retriever() with custom search_kwargs in SPARSE mode."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 390)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore = QdrantVectorStore.from_texts(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 408)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/test_add_texts.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foobar", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/test_from_texts.py` (line 259)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/test_similarity_search.py` (line 19)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_qdrant_similarity_search(
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/integration_tests/test_similarity_search.py` (line 36)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/unit_tests/test_imports.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"QdrantVectorStore",
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/unit_tests/test_standard.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_qdrant import QdrantVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/unit_tests/test_standard.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test QdrantVectorStore initialization time."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/partners/qdrant/tests/unit_tests/test_standard.py` (line 26)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore.from_texts(
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/xai/langchain_xai/chat_models.py` (line 537)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"xAI API key is not set. Please set it in the `xai_api_key` field or "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/xai/langchain_xai/chat_models.py` (line 538)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"in the `XAI_API_KEY` environment variable."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/partners/xai/tests/unit_tests/test_chat_models.py` (line 37)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test that streaming correctly invokes on_llm_new_token callback."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/__init__.py` (line 40)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/__init__.py` (line 56)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"VectorStoreIntegrationTests",
```

### [HIGH] Dangerous execution pattern: os.system() call
- **File:** `libs/standard-tests/langchain_tests/integration_tests/sandboxes.py` (line 1191)
- **Category:** os_system
- **OWASP:** LLM07 — Insecure Plugin Design

```
malicious_path = "'; import os; os.system('echo INJECTED'); #"
```

### [HIGH] Dangerous execution pattern: os.system() call
- **File:** `libs/standard-tests/langchain_tests/integration_tests/sandboxes.py` (line 1203)
- **Category:** os_system
- **OWASP:** LLM07 — Insecure Plugin Design

```
malicious_path = "'; import os; os.system('echo INJECTED'); #"
```

### [HIGH] LLM call with nearby user input and no visible sanitisation
- **File:** `libs/standard-tests/langchain_tests/integration_tests/tools.py` (line 32)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01 — Prompt Injection

```
result = tool.invoke(tool_call)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 1)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test suite to test `VectorStore` integrations."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 8)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 21)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreIntegrationTests(BaseStandardTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 36)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 37)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_parrot_link.vectorstores import ParrotVectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 38)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 69)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestChromaStandard(VectorStoreIntegrationTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 71)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 72)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
\"\"\"Get an empty VectorStore for unit tests.\"\"\"
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 86)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestParrotVectorStore(VectorStoreIntegrationTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 88)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 102)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> VectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 103)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Get the `VectorStore` class to test.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 105)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
The returned `VectorStore` should be empty.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 120)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Whether the `VectorStore` supports `get_by_ids`."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 138)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_vectorstore_is_empty(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 139)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test that the `VectorStore` is empty.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 144)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStoreIntegrationTests`) initializes an empty vector store in the
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 150)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert vectorstore.similarity_search("foo", k=1) == []
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 152)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_add_documents(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 153)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test adding documents into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 174)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = vectorstore.similarity_search("bar", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 186)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_vectorstore_still_empty(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 187)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test that the `VectorStore` is still empty.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 197)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStoreIntegrationTests`) correctly clears the vector store in the
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 203)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert vectorstore.similarity_search("foo", k=1) == []
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 205)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_deleting_documents(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 206)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test deleting documents from the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 224)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = vectorstore.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 227)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_deleting_bulk_documents(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 246)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = vectorstore.similarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 249)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_delete_missing_content(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 264)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 283)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = vectorstore.similarity_search("bar", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 289)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_add_documents_by_id_with_mutation(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 318)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = vectorstore.similarity_search("new foo", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 328)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_get_by_ids(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 339)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 369)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_get_by_ids_missing(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 378)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 399)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_add_documents_documents(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 411)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 440)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_add_documents_with_existing_ids(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 456)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 486)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_vectorstore_is_empty_async(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 487)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test that the `VectorStore` is empty.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 492)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStoreIntegrationTests`) initializes an empty vector store in the
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 498)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert await vectorstore.asimilarity_search("foo", k=1) == []
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 500)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_add_documents_async(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 501)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test adding documents into the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 522)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = await vectorstore.asimilarity_search("bar", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 536)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 538)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test that the `VectorStore` is still empty.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 548)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`VectorStoreIntegrationTests`) correctly clears the vector store in the
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 554)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert await vectorstore.asimilarity_search("foo", k=1) == []
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 556)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_deleting_documents_async(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 557)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Test deleting documents from the `VectorStore`.
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 575)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = await vectorstore.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 579)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 599)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = await vectorstore.asimilarity_search("foo", k=1)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 602)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_delete_missing_content_async(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 617)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 636)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = await vectorstore.asimilarity_search("bar", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 643)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 673)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
documents = await vectorstore.asimilarity_search("new foo", k=2)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 683)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_get_by_ids_async(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 694)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 724)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def test_get_by_ids_missing_async(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 733)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 754)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 767)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 797)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self, vectorstore: VectorStore
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 814)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
`get_by_ids` was added to the `VectorStore` interface in
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 5)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
InMemoryVectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 6)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
VectorStore,
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 9)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 12)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestInMemoryVectorStore(VectorStoreIntegrationTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 14)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> VectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 16)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return InMemoryVectorStore(embedding=embeddings)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 19)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class WithoutGetByIdsVectorStore(InMemoryVectorStore):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 20)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""InMemoryVectorStore that does not implement get_by_ids."""
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 22)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
get_by_ids = VectorStore.get_by_ids
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 25)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestWithoutGetByIdVectorStore(VectorStoreIntegrationTests):
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 27)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> VectorStore:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 29)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return WithoutGetByIdsVectorStore(embedding=embeddings)
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 35)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def test_get_by_ids_fails(self, vectorstore: VectorStore) -> None:
```

### [HIGH] RAG retrieval with no visible sanitisation of retrieved content
- **File:** `libs/standard-tests/tests/unit_tests/test_in_memory_vectorstore.py` (line 38)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
match="WithoutGetByIdsVectorStore does not yet support get_by_ids",
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/langchain_text_splitters/base.py` (line 259)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"This is needed in order to calculate max_tokens_for_prompt. "
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/langchain_text_splitters/base.py` (line 421)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Maximum number of tokens per chunk"""
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/langchain_text_splitters/base.py` (line 444)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "tokens_per_chunk must be greater than chunk_overlap"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/langchain_text_splitters/nltk.py` (line 47)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
msg = "When use_span_tokenize is True, separator should be ''"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/langchain_text_splitters/sentence_transformers.py` (line 71)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f" is: {self.maximum_tokens_per_chunk}."
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/langchain_text_splitters/sentence_transformers.py` (line 72)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
f" Argument tokens_per_chunk={self.tokens_per_chunk}"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/tests/integration_tests/test_nlp_text_splitters.py` (line 95)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
ValueError, match="When use_span_tokenize is True, separator should be ''"
```

### [HIGH] High-entropy string in a credential-like variable
- **File:** `libs/text-splitters/tests/integration_tests/test_text_splitter.py` (line 25)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06 — Sensitive Information Disclosure

```
"""Test text splitter that uses a HuggingFace tokenizer."""
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 31)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class _VectorStoreExampleSelector(BaseExampleSelector, BaseModel, ABC):
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 34)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vectorstore: VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 35)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""VectorStore that contains information about examples."""
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 48)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Extra arguments passed to similarity_search function of the `VectorStore`."""
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 168)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
of the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 212)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
of the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 302)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
of the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 349)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
of the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 299)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore | DocumentIndex,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 349)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: `VectorStore` or DocumentIndex to index the documents into.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 387)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
method of the `VectorStore` or the upsert method of the DocumentIndex.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 399)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ValueError: If `VectorStore` does not have
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 402)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
TypeError: If `vectorstore` is not a `VectorStore` or a DocumentIndex.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 427)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(destination, VectorStore):
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 638)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore | DocumentIndex,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 688)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: `VectorStore` or DocumentIndex to index the documents into.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 726)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
method of the `VectorStore` or the upsert method of the DocumentIndex.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 738)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
ValueError: If `VectorStore` does not have
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 741)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
TypeError: If `vector_store` is not a `VectorStore` or DocumentIndex.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/indexing/api.py` (line 766)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
if isinstance(destination, VectorStore):
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 930)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
Retriever class for `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 936)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch.as_retriever(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 946)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch.as_retriever(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 952)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch.as_retriever(search_kwargs={"k": 1})
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 955)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch.as_retriever(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 961)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
return VectorStoreRetriever(vectorstore=self, tags=tags, **kwargs)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 964)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class VectorStoreRetriever(BaseRetriever):
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 965)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Base Retriever class for VectorStore."""
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 89)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = vector_store.similarity_search(query="thud", k=1)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 104)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = vector_store.similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 622)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 672)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 974)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1024)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1959)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 1979)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2162)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(vector_store, InMemoryVectorStore)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2171)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2219)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
record_manager: InMemoryRecordManager, vector_store: VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2269)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2317)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
arecord_manager: InMemoryRecordManager, vector_store: InMemoryVectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/indexing/test_indexing.py` (line 2403)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(vector_store, InMemoryVectorStore)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 95)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
loaded_store = InMemoryVectorStore.load(test_file, embedding)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 96)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
loaded_output = loaded_store.similarity_search("foo", k=1)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 103)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = await InMemoryVectorStore.afrom_texts(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 110)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = store.similarity_search("fee", filter=lambda doc: doc.metadata["id"] == 1)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 114)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await store.asimilarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 123)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = InMemoryVectorStore(embedding=embedding)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 134)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = store.similarity_search("document", filter=lambda doc: doc.id == "doc_2")
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 140)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await store.asimilarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 148)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = store.similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/core/tests/unit_tests/vectorstores/test_in_memory.py` (line 157)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = InMemoryVectorStore(embedding=embedding)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/langchain_classic/memory/vectorstore_token_buffer_memory.py` (line 120)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
self._memory_retriever = VectorStoreRetrieverMemory(retriever=self.retriever)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/langchain_classic/vectorstores/redis/__init__.py` (line 7)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_community.vectorstores.redis.base import RedisVectorStoreRetriever
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/langchain_classic/vectorstores/redis/__init__.py` (line 24)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RedisVectorStoreRetriever": "langchain_community.vectorstores.redis.base",
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/langchain_classic/vectorstores/redis/__init__.py` (line 41)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RedisVectorStoreRetriever",
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/chains/test_imports.py` (line 30)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"MultiRetrievalQAChain",
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/chains/test_imports.py` (line 42)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RetrievalQA",
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/chains/test_imports.py` (line 43)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"RetrievalQAWithSourcesChain",
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 419)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 464)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 513)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1145)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1161)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1176)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1227)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: VectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1270)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
vector_store: InMemoryVectorStore,
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/indexes/test_indexing.py` (line 1342)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
assert isinstance(vector_store, InMemoryVectorStore)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/retrievers/self_query/test_base.py` (line 64)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class InMemoryVectorstoreWithSearch(InMemoryVectorStore):
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/langchain/tests/unit_tests/retrievers/self_query/test_base.py` (line 66)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 235)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = vector_store.similarity_search(query="thud", k=1)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 245)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = vector_store.similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 515)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Run more images through the embeddings and add to the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 604)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Run more texts through the embeddings and add to the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 607)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
texts: Texts to add to the `VectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 730)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 240)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output1 = docsearch.similarity_search("far", k=1, filter={"first_letter": "f"})
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 241)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output2 = docsearch.similarity_search("far", k=1, filter={"first_letter": "b"})
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 303)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# Get a new VectorStore from the persisted directory
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 309)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 350)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
# Get a new VectorStore from the persisted directory
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/chroma/tests/integration_tests/test_vectorstores.py` (line 356)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 124)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
results = vector_store.similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 225)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Initialize a new instance of `QdrantVectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 372)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> QdrantVectorStore:
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 373)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Construct an instance of `QdrantVectorStore` from a list of texts.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 435)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 459)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> QdrantVectorStore:
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 460)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"""Construct `QdrantVectorStore` from existing collection without adding data.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 463)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
QdrantVectorStore: A new instance of `QdrantVectorStore`.
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 520)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 909)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
) -> QdrantVectorStore:
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1151)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1180)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1249)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
raise QdrantVectorStoreError(msg)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1253)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1271)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
raise QdrantVectorStoreError(msg)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 1275)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
cls: type[QdrantVectorStore],
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 17)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 225)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/langchain_qdrant/vectorstores.py` (line 284)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
async def asimilarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/async_api/test_similarity_search.py` (line 122)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await docsearch.asimilarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/async_api/test_similarity_search.py` (line 266)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = await docsearch.asimilarity_search("foo", k=1, filter=qdrant_filter)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 104)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "bar"]
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 118)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 135)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1, filter=qdrant_filter)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 204)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
@pytest.mark.parametrize("content_payload_key", [QdrantVectorStore.CONTENT_KEY, "foo"])
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 206)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "bar"]
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 221)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
docsearch = QdrantVectorStore.from_texts(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 255)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
@pytest.mark.parametrize("content_payload_key", [QdrantVectorStore.CONTENT_KEY, "foo"])
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 257)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
"metadata_payload_key", [QdrantVectorStore.METADATA_KEY, "bar"]
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/qdrant_vector_store/test_search.py` (line 302)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1, filter=qdrant_filter)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/test_similarity_search.py` (line 115)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search(
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/partners/qdrant/tests/integration_tests/test_similarity_search.py` (line 246)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
output = docsearch.similarity_search("foo", k=1, filter=qdrant_filter)
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 41)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
class TestParrotVectorStore(VectorStoreIntegrationTests):
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 43)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
def vectorstore(self) -> Generator[VectorStore, None, None]:  # type: ignore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 45)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
store = ParrotVectorStore(self.get_embeddings())
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 63)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_core.vectorstores import VectorStore
```

### [MEDIUM] RAG retrieval detected - verify retrieved content is sanitised before LLM injection
- **File:** `libs/standard-tests/langchain_tests/integration_tests/vectorstores.py` (line 64)
- **Category:** unsafe_rag
- **OWASP:** LLM01 — Prompt Injection

```
from langchain_tests.integration_tests.vectorstores import VectorStoreIntegrationTests
```

### [LOW] LLM call near user input - sanitisation detected but verify it's sufficient
- **File:** `.github/workflows/check_release_deps.yml` (line 117)
- **Category:** prompt_injection_possible
- **OWASP:** LLM01 — Prompt Injection

```
shown = subprocess.run(
```

### [LOW] LLM call near user input - sanitisation detected but verify it's sufficient
- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 217)
- **Category:** prompt_injection_possible
- **OWASP:** LLM01 — Prompt Injection

```
self.response_chain.invoke(
```
