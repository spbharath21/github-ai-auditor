# AI Security Audit Report

**Repository:** hwchase17/langchain
**Files Scanned:** 2580
**Security Score:** 0/100 — Critical Risk
**Total Findings:** 415

---

## Summary

| Severity | Count |
|----------|-------|
| Critical | 3 |
| High     | 406 |
| Medium   | 5 |
| Low      | 1 |

---

## OWASP LLM Top 10 Coverage


- **LLM01**: 58 finding(s)

- **LLM06**: 351 finding(s)

- **LLM07**: 5 finding(s)


---

## Findings


### [CRITICAL] Hardcoded OpenAI API key detected

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_pii.py` (line 539)
- **Category:** hardcoded_secret
- **OWASP:** LLM06
state = AgentState[Any](messages=[HumanMessage("Key: sk-abcdefghijklmnopqrstuvwxyz123456")])

### [CRITICAL] Hardcoded OpenAI API key detected

- **File:** `libs/langchain_v1/tests/unit_tests/agents/test_create_agent_tool_validation.py` (line 294)
- **Category:** hardcoded_secret
- **OWASP:** LLM06
"api_key": "sk-secret-key-abc123xyz",

### [CRITICAL] Hardcoded OpenAI API key detected

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 150)
- **Category:** hardcoded_secret
- **OWASP:** LLM06
_build_model(**{field: "sk-should-not-be-allowed"})

### [HIGH] Dangerous execution pattern: exec() call

- **File:** `.github/workflows/close_unchecked_issues.yml` (line 68)
- **Category:** exec_usage

const headingMatch = headingRe.exec(body);

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 115)
- **Category:** unsafe_rag
- **OWASP:** LLM01
example_docs = self.vectorstore.similarity_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 135)
- **Category:** unsafe_rag
- **OWASP:** LLM01
example_docs = await self.vectorstore.asimilarity_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/example_selectors/semantic_similarity.py` (line 250)
- **Category:** unsafe_rag
- **OWASP:** LLM01
example_docs = self.vectorstore.max_marginal_relevance_search(

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/language_models/base.py` (line 104)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Encode the text into token IDs using the fallback GPT-2 tokenizer."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/language_models/base.py` (line 108)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Using fallback GPT-2 tokenizer for token counting. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/language_models/base.py` (line 109)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Token counts may be inaccurate for non-GPT-2 models. "

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/langchain_core/language_models/llms.py` (line 524)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
yield self.invoke(input, config=config, stop=stop, **kwargs)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/language_models/model_profile.py` (line 52)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Maximum context window (tokens)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/messages/base.py` (line 115)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Examples: response headers, logprobs, token counts, model name."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/messages/utils.py` (line 1375)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"type": "text", "text": "This is the FIRST 4 token block."},

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/messages/utils.py` (line 1376)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"type": "text", "text": "This is the SECOND 4 token block."},

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/messages/utils.py` (line 1435)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
[{"type": "text", "text": "This is the FIRST 4 token block."}],

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/messages/utils.py` (line 1487)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"{type(actual_token_counter)}."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/messages/utils.py` (line 2400)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Wrapper for `count_tokens_approximately` that matches expected signature."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/output_parsers/openai_tools.py` (line 299)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Output parser received a `max_tokens` stop reason. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/output_parsers/openai_tools.py` (line 300)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"The output is likely incomplete—please increase `max_tokens` "

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/langchain_core/prompts/chat.py` (line 813)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
prompt_value = template.invoke(

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/langchain_core/prompts/chat.py` (line 887)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
prompt_value = template.invoke("Hello, there!")

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/retrievers.py` (line 257)
- **Category:** unsafe_rag
- **OWASP:** LLM01
await retriever.ainvoke("query")

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/tools/retriever.py` (line 79)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = await retriever.ainvoke(query, config={"callbacks": callbacks})

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/langchain_core/tracers/log_stream.py` (line 62)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""List of LLM tokens streamed by this run, if applicable."""

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 311)
- **Category:** unsafe_rag
- **OWASP:** LLM01
return self.similarity_search(query, **kwargs)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 318)
- **Category:** unsafe_rag
- **OWASP:** LLM01
return self.max_marginal_relevance_search(query, **kwargs)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 346)
- **Category:** unsafe_rag
- **OWASP:** LLM01
return await self.asimilarity_search(query, **kwargs)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1045)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = self.vectorstore.similarity_search(query, **kwargs_)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1054)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = self.vectorstore.max_marginal_relevance_search(query, **kwargs_)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/core/langchain_core/vectorstores/base.py` (line 1070)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = await self.vectorstore.asimilarity_search(query, **kwargs_)

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/tests/unit_tests/language_models/chat_models/test_base.py` (line 972)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
response = llm.invoke("hello")

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/tests/unit_tests/language_models/chat_models/test_base.py` (line 977)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
response = llm.invoke("hello")

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 60)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"Secret was leaked in deserialized object! Found '{SENTINEL_VALUE}'.\n"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 69)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`HumanMessage` with secret-like dict in `content`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 79)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`HumanMessage` with secret-like dict in `additional_kwargs`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 87)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`HumanMessage` with secret-like dict nested in `additional_kwargs`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 95)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`HumanMessage` with secret-like dict in a list in `additional_kwargs`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 103)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`AIMessage` with secret-like dict in respo`nse_metadata."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 111)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Document with secret-like dict in `metadata`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 119)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`AIMessage` containing `dumpd(HumanMessage)` with secret in kwargs."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 135)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Dict containing a `Serializable` with secret-like dict."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 144)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Dict with secret-like dict, no `Serializable` objects."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 149)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Dict with nested secret-like dict, no `Serializable` objects."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 176)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Pydantic model containing a `Serializable` with secret-like dict."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 218)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Custom class containing a `Serializable` with secret-like dict."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 233)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Custom class containing a secret-like dict directly."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 253)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`AIMessage` with `dumpd(HumanMessage w/ secret)` in `additional_kwargs`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/load/test_secret_injection.py` (line 290)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Verify secret-like dict in `Document` metadata is preserved."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 277)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"type": "text", "text": "This is the FIRST 4 token block."},

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 278)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"type": "text", "text": "This is the SECOND 4 token block."},

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 308)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
[{"type": "text", "text": "This is the FIRST 4 token block."}], id="second"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 363)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"type": "text", "text": "This is the SECOND 4 token block."},

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 389)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"type": "text", "text": "This is the SECOND 4 token block."},

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 711)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that invalid `token_counter` shortcut raises `ValueError`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 962)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
return "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgy

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2766)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test approximate token counting with image content blocks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2780)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert token_count < 200, f"Expected <200 tokens, got {token_count}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2781)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert token_count > 80, f"Expected >80 tokens, got {token_count}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/messages/test_utils.py` (line 2850)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that unknown multimodal block types still contribute to token count."""

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/tests/unit_tests/prompts/test_chat.py` (line 350)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
result = template.invoke({"name": "Alice", "question": "Hello?"})

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/core/tests/unit_tests/prompts/test_dict.py` (line 45)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
template={"output": "{message.additional_kwargs[secret]}"},

### [HIGH] Dangerous execution pattern: __import__ dynamic import

- **File:** `libs/core/tests/unit_tests/prompts/test_loading.py` (line 331)
- **Category:** dynamic_import
- **OWASP:** LLM07
".__import__('os').popen('id').read() }}"

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/core/tests/unit_tests/runnables/test_tracing_interops.py` (line 615)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
return chain.invoke(x, config={"callbacks": [tracer]})

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/agents/openai_assistant/base.py` (line 673)
- **Category:** unsafe_rag
- **OWASP:** LLM01
run = self.client.beta.threads.runs.retrieve(run_id, thread_id=thread_id)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/agents/openai_assistant/base.py` (line 826)
- **Category:** unsafe_rag
- **OWASP:** LLM01
run = await self.async_client.beta.threads.runs.retrieve(

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/langchain_classic/agents/openai_functions_agent/base.py` (line 125)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
predicted_message = self.llm.invoke(

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/langchain_classic/agents/openai_functions_agent/base.py` (line 131)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
predicted_message = self.llm.invoke(

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/langchain_classic/agents/openai_functions_multi_agent/base.py` (line 228)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
predicted_message = self.llm.invoke(

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/callbacks/streaming_stdout_final_only.py` (line 82)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Run on new LLM token. Only available when streaming is enabled."""

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 431)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = await self.retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/conversational_retrieval/base.py` (line 531)
- **Category:** unsafe_rag
- **OWASP:** LLM01
return self.vectorstore.similarity_search(

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 32)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Extract tokens and log probabilities from chat model response."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 115)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Minimum probability for a token to be considered low confidence."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 117)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Minimum number of tokens between two low confidence spans."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 119)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Number of tokens to pad around a low confidence span."""

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 145)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
docs.extend(self.retriever.invoke(question))

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 147)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
result = self.response_chain.invoke(

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 299)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"FlareChain.from_llm: supplied llm max_completion_tokens=%s "

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/langchain_classic/chains/llm.py` (line 61)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
chain.invoke("your adjective here")

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/chains/natbot/base.py` (line 82)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"model = OpenAI(temperature=0.5, best_of=10, n=3, max_tokens=50)"

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/retrieval.py` (line 66)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = await self.retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/qa_with_sources/vector_db.py` (line 60)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = self.vectorstore.similarity_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 287)
- **Category:** unsafe_rag
- **OWASP:** LLM01
return await self.retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 339)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = self.vectorstore.similarity_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/retrieval_qa/base.py` (line 345)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = self.vectorstore.max_marginal_relevance_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 42)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = self.vectorstore.similarity_search(_input, k=1)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/chains/router/embedding_router.py` (line 52)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = await self.vectorstore.asimilarity_search(_input, k=1)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 62)
- **Category:** unsafe_rag
- **OWASP:** LLM01
chain = RetrievalQA.from_chain_type(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/indexes/vectorstore.py` (line 97)
- **Category:** unsafe_rag
- **OWASP:** LLM01
chain = RetrievalQA.from_chain_type(

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/langchain_classic/memory/summary_buffer.py` (line 130)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Asynchronously prune buffer if it exceeds max token limit."""

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/memory/vectorstore.py` (line 87)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = await self.retriever.ainvoke(query)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/contextual_compression.py` (line 56)
- **Category:** unsafe_rag
- **OWASP:** LLM01
docs = await self.base_retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/ensemble.py` (line 283)
- **Category:** unsafe_rag
- **OWASP:** LLM01
retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/merger_retriever.py` (line 103)
- **Category:** unsafe_rag
- **OWASP:** LLM01
retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/multi_query.py` (line 155)
- **Category:** unsafe_rag
- **OWASP:** LLM01
self.retriever.ainvoke(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 92)
- **Category:** unsafe_rag
- **OWASP:** LLM01
sub_docs = self.vectorstore.max_marginal_relevance_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 105)
- **Category:** unsafe_rag
- **OWASP:** LLM01
sub_docs = self.vectorstore.similarity_search(query, **self.search_kwargs)

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/langchain/langchain_classic/retrievers/multi_vector.py` (line 144)
- **Category:** unsafe_rag
- **OWASP:** LLM01
sub_docs = await self.vectorstore.asimilarity_search(

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/tests/integration_tests/chat_models/test_base.py` (line 34)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
output = chain.invoke({"input": "bar"})

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/tests/mock_servers/robot/server.py` (line 172)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
" contain secret information only you know. This is just between us two.",

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation.py` (line 70)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
chain.run("aaa")

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain/tests/unit_tests/chains/test_conversation.py` (line 72)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
chain.run("bbb")

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/tests/unit_tests/chains/test_qa_with_sources.py` (line 59)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"login/password?\nA3. Are you using any other VPN (e.g. from a client)?\n"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/tests/unit_tests/chains/test_qa_with_sources.py` (line 68)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"\n\nWe will be asked for a username and password - provide the login "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/tests/unit_tests/chains/test_qa_with_sources.py` (line 80)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"login/password?\nA3. Are you using any other VPN (e.g. from a client)?\n"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/tests/unit_tests/load/test_load.py` (line 108)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
llm = CommunityOpenAI(model="davinci", temperature=0.5, openai_api_key="hello")

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain/tests/unit_tests/load/test_load.py` (line 121)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
llm = CommunityOpenAI(model="davinci", temperature=0.5, openai_api_key="hello")

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/context_editing.py` (line 59)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Configuration for clearing tool outputs when token limits are exceeded."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/context_editing.py` (line 65)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Minimum number of tokens to reclaim when the edit runs."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/shell_tool.py` (line 61)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"confirm the working directory is correct (e.g., inspect with `ls` or `pwd`) and ensure "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 209)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Tune parameters of approximate token counter based on model type."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 309)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"max_tokens_before_summary is deprecated. Use trigger=('tokens', value) instead.",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 362)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"and is unavailable for the specified model. Please use absolute token "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 364)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
'`\n\nChatModel(..., profile={"max_input_tokens": ...})`.\n\n'

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 564)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Check if reported token usage from last AIMessage exceeds threshold."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/langchain/agents/middleware/summarization.py` (line 584)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Determine whether summarization should run for the current token usage."""

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/langchain_v1/tests/integration_tests/chat_models/test_base.py` (line 32)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
output = chain.invoke({"input": "bar"})

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 246)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
with pytest.warns(DeprecationWarning, match="max_tokens_before_summary is deprecated"):

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 376)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Ensure token retention preserves AI/Tool message pairs together."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 760)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test binary search in _find_token_based_cutoff with edge cases."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 889)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test handling of edge cases with target token calculations."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 995)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
with pytest.warns(DeprecationWarning, match="max_tokens_before_summary is deprecated"):

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1079)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"langchain.agents.middleware.summarization.count_tokens_approximately",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1692)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""A clause combining `tokens` and `fraction` (no `messages`) is AND-evaluated."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1753)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"get_buffer_string should produce fewer tokens than count_tokens_approximately. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1761)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"str(messages) should produce significantly more tokens. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_summarization.py` (line 1994)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Fraction triggers should account for provider-reported token usage."""

### [HIGH] Dangerous execution pattern: eval() with non-literal argument

- **File:** `libs/langchain_v1/tests/unit_tests/agents/middleware/implementations/test_tool_emulator.py` (line 40)
- **Category:** eval_usage
- **OWASP:** LLM07
return f"Result: {eval(expression)}"  # noqa: S307

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/langchain_v1/tests/unit_tests/agents/test_create_agent_tool_validation.py` (line 410)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Error should NOT contain password value (from system-injected state)"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 931)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Number of most likely tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 934)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Total probability mass of tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 963)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Automatically read from env var `ANTHROPIC_API_KEY` if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 1096)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return a mapping of secret keys to environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/chat_models.py` (line 1155)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Set default `max_tokens` from model profile with fallback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 40)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Number of most likely tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 43)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Total probability mass of tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 72)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Automatically read from env var `ANTHROPIC_API_KEY` if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 161)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return a mapping of secret keys to environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/langchain_anthropic/llms.py` (line 418)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"ChatAnthropic.get_num_tokens_from_messages instead."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 51)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from Anthropic."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 97)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from Anthropic."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 375)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 391)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 433)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from Anthropic."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_chat_models.py` (line 449)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from Anthropic."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_llms.py` (line 46)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/integration_tests/test_llms.py` (line 67)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/unit_tests/test_chat_models.py` (line 139)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test the set_default_max_tokens function."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/unit_tests/test_chat_models.py` (line 2917)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
message="prompt is too long: 209752 tokens > 200000 maximum",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/anthropic/tests/unit_tests/test_chat_models.py` (line 2923)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"message": "prompt is too long: 209752 tokens > 200000 maximum",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/deepseek/langchain_deepseek/chat_models.py` (line 244)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "If using default api base, DEEPSEEK_API_KEY must be set."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/exa/langchain_exa/tools.py` (line 79)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
content="Title: San Francisco, CA Weather Conditionsstar_ratehome\nURL: https://www.wunderground.com/weather/37.8,-122.4

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/langchain_fireworks/chat_models.py` (line 744)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"You can pass it an argument as `api_key=...` or "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/langchain_fireworks/chat_models.py` (line 745)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"set the environment variable `FIREWORKS_API_KEY`."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/langchain_fireworks/embeddings.py` (line 76)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"You can pass it an argument as `api_key=...` or "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/langchain_fireworks/embeddings.py` (line 77)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"set the environment variable `FIREWORKS_API_KEY`."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/langchain_fireworks/llms.py` (line 48)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"You can pass it an argument as `api_key=...` or "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/langchain_fireworks/llms.py` (line 49)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"set the environment variable `FIREWORKS_API_KEY`."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 64)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from ChatFireworks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 84)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Expected exactly one chunk with token counts or response_metadata. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 103)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from ChatFireworks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 114)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test invoke tokens from ChatFireworks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_chat_models.py` (line 122)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test invoke tokens from ChatFireworks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 49)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 57)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 74)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from Fireworks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/integration_tests/test_llms.py` (line 85)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from Fireworks."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/fireworks/tests/unit_tests/test_chat_models.py` (line 1061)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""When provider omits total_tokens, sum input + output."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/langchain_groq/chat_models.py` (line 400)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
alias="api_key", default_factory=secret_from_env("GROQ_API_KEY", default=None)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/langchain_groq/chat_models.py` (line 402)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Automatically inferred from env var `GROQ_API_KEY` if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/langchain_groq/chat_models.py` (line 564)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Mapping of secret environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 60)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test ainvoke tokens from ChatGroq."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 70)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from ChatGroq."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 81)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test abatch tokens from ChatGroq."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 120)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Expected exactly one chunk with token counts or metadata. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 183)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/integration_tests/test_chat_models.py` (line 200)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 308)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
llm = ChatGroq(model="foo", api_key=secret, model_kwargs={"not_secret": not_secret})  # type: ignore[call-arg, arg-type]

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 464)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that explicit total_tokens=0 is preserved, not replaced by sum."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 477)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that input_tokens=0 is not overridden by prompt_tokens fallback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 491)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that output_tokens=0 is not overridden by completion_tokens fallback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 523)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that zero cached tokens are not included (falsy)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 587)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that zero reasoning tokens are not included (falsy)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 667)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that _create_chat_result properly includes reasoning tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 713)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that _create_chat_result includes both cached and reasoning tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 846)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming properly includes reasoning tokens in usage metadata."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/groq/tests/unit_tests/test_chat_models.py` (line 962)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that _combine_llm_outputs properly combines nested token details."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 496)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Tokenizer for the model. Only used for HuggingFacePipeline."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 506)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Penalizes repeated tokens according to frequency."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 516)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Modify the likelihood of specified tokens appearing in the completion."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 525)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Total probability mass of tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/langchain_huggingface/chat_models/huggingface.py` (line 1033)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Make sure that your Hugging Face token has access to the endpoint."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/langchain_huggingface/llms/huggingface_endpoint.py` (line 143)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Stop generating tokens if a member of `stop_sequences` is generated"""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/tests/integration_tests/test_llms.py` (line 7)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from huggingface_pipeline."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/tests/unit_tests/test_chat_models.py` (line 236)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that _default_params includes inherited max_tokens from max_new_tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/huggingface/tests/unit_tests/test_huggingface_endpoint.py` (line 67)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""HF-hosted endpoint_url still gets the token."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 210)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Could not download mistral tokenizer from Huggingface for "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 211)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"calculating batch sizes. Set a Huggingface token via the "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 212)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"HF_TOKEN environment variable to download the real tokenizer. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/mistralai/langchain_mistralai/embeddings.py` (line 220)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Split list of texts into batches of less than 16k tokens for Mistral API."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/mistralai/tests/integration_tests/test_chat_models.py` (line 20)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from ChatMistralAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/mistralai/tests/integration_tests/test_chat_models.py` (line 38)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Expected exactly one chunk with token counts or response_metadata. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 32)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch sync token generation from `OllamaLLM`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 41)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch async token generation from `OllamaLLM`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 72)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming raw string tokens from `OllamaLLM`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/integration_tests/test_llms.py` (line 80)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test async streaming raw string tokens from `OllamaLLM`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 1)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URL authentication parsing functionality."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 15)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test the parse_url_with_auth utility function."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 23)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URLs without authentication credentials."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 36)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URLs with authentication credentials."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 37)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url = "https://user:password@ollama.example.com:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 62)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test scheme-less URL with authentication credentials."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 63)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url = "user:password@ollama.example.com:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 74)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URLs with auth, path, and query parameters."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 99)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URLs with only username (no password)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 111)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URLs with empty password."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 124)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URL authentication integration with ChatOllama."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 131)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that ChatOllama properly handles URL authentication."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 132)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url_with_auth = "https://user:password@ollama.example.com:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 155)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url_with_auth = "https://user:password@ollama.example.com:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 179)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URL authentication integration with OllamaLLM."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 186)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that OllamaLLM properly handles URL authentication."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 187)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url_with_auth = "https://user:password@ollama.example.com:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 205)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test URL authentication integration with OllamaEmbeddings."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 212)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that OllamaEmbeddings properly handles URL authentication."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 213)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url_with_auth = "https://user:password@ollama.example.com:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 242)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url = "https://user:password@ollama.example.com"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 279)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
url = "https://user:password@[::1]:11434"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/ollama/tests/unit_tests/test_auth.py` (line 297)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test with complex passwords containing special characters."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/azure.py` (line 495)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Automatically inferred from env var `AZURE_OPENAI_API_KEY` if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/azure.py` (line 588)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Get the mapping of secret environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 495)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"{type(new_usage)} and {type(overall_token_usage)}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 503)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"{type(new_usage)} and {type(overall_token_usage)}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 510)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
warnings.warn(f"Unexpected type for token usage: {type(new_usage)}")

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 525)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
or "Input tokens exceed the configured limit" in e.message

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 613)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 718)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Penalizes repeated tokens according to frequency."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 734)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Modify the likelihood of specified tokens appearing in the completion."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 743)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Total probability mass of tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 2097)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"get_num_tokens_from_messages() is not presently implemented "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 2099)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"https://platform.openai.com/docs/guides/text-generation/managing-tokens"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/base.py` (line 3322)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Mapping of secret environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 69)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"subscription OAuth against Codex endpoints and must only be used where "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 386)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"`_ChatGPTOAuthTokenProvider` protocol."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 400)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"`_ChatOpenAICodex` manages authentication via "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 401)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"`token_provider`; drop the explicit `{key}=`. Use "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 402)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"`ChatOpenAI` if you want API-key authentication."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chat_models/codex.py` (line 536)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`_ChatOpenAICodex` is not serializable (holds a live token provider)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 61)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
CHATGPT_DEVICE_REDIRECT_URI = "https://auth.openai.com/deviceauth/callback"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 95)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Validate non-empty secrets and timezone-aware `expires_at`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 97)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "`access_token` must be a non-empty string."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 100)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "`refresh_token` must be a non-empty string."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 107)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return `True` if the token is past (or within `skew` of) expiry."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 122)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Refresh-aware token source consumed by `_ChatOpenAICodex`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 137)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return only the access token string (sync callable for SDKs)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 141)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return only the access token string (async callable for SDKs)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 175)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Pull the ChatGPT account/plan/user IDs out of an ID-token JWT."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 195)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"id_token; the `ChatGPT-Account-Id` header will be omitted."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 205)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = f"OAuth token response had invalid `expires_in`: {raw!r}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 209)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"OAuth token response had missing or non-positive `expires_in`; "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 210)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"refusing to store an immediately-expired token."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 221)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Build a `_ChatGPTToken` from an OAuth token-endpoint response."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 223)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "OAuth token response did not include an `access_token`."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 231)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"prior refresh token was available; re-run `login_chatgpt()`."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 336)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"fcntl is unavailable on this platform; ChatGPT token store "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 370)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return `(error_code, body_excerpt)` from an OAuth error response."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 389)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"ChatGPT refresh token is no longer valid (`invalid_grant`). "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 390)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Re-run `login_chatgpt()` to obtain a new token."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 393)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = f"OAuth request to {url} failed with status {resp.status_code}: {excerpt}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 506)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"Failed to read ChatGPT token store at {self.path}: {exc}. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 515)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"ChatGPT token store at {self.path} is not valid JSON: "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 523)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"ChatGPT token store at {self.path} is missing required "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 555)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Refreshing ChatGPT access token (refresh_token=%s).",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 569)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"No ChatGPT OAuth token found at {self.path}. Run "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 570)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"`langchain_openai.chatgpt_oauth.login_chatgpt()` first."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 632)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Return only the access-token string (async)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 667)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
return f"{CHATGPT_AUTHORIZE_URL}?{urllib.parse.urlencode(params)}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 701)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"ChatGPT OAuth callback returned error %r (%s)",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 801)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"Could not bind ChatGPT OAuth callback server on "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 817)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = f"Timed out waiting for ChatGPT OAuth callback on http://{host}:{port}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 844)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"`host={host!r}` is not a loopback address. The OAuth callback "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 911)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f"\nChatGPT sign-in: open the following URL in a browser:\n  {authorize_url}\n"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 913)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
logger.info("Opening ChatGPT sign-in flow at %s", CHATGPT_AUTHORIZE_URL)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 930)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "ChatGPT OAuth callback state mismatch."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 934)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = f"ChatGPT OAuth callback returned error: {result['error']} {description}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 938)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "ChatGPT OAuth callback did not include an authorization code."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 1031)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = f"Device authorization failed: {error}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/chatgpt_oauth.py` (line 1035)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "Timed out waiting for ChatGPT device authorization."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/embeddings/azure.py` (line 125)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Automatically inferred from env var `AZURE_OPENAI_API_KEY` if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/embeddings/base.py` (line 23)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""API limit per request for embedding tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/embeddings/base.py` (line 238)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/azure.py` (line 110)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Mapping of secret keys to environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 188)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Total probability mass of tokens to consider at each step."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 191)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Penalizes repeated tokens according to frequency."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 206)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 208)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Automatically inferred from env var `OPENAI_API_KEY` if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 246)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Adjust the probability of specific tokens being generated."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 601)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "max_tokens set to -1 not supported for multiple inputs."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 681)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"(e.g. `ChatOpenAI(model=...).profile['max_input_tokens']`)"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 746)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Profile for model %s is missing `max_input_tokens`; "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 757)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"name, or read `max_input_tokens` from the model profile directly. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/langchain_openai/llms/base.py` (line 903)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Mapping of secret keys to environment variables."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/conftest.py` (line 60)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Redact OAuth secret fields in a urlencoded form body."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/conftest.py` (line 148)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Scrubbed a JWT-shaped token from a non-UTF-8 response body "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/conftest.py` (line 80)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Stub `_FileChatGPTOAuthTokenProvider` token reads for Codex VCR tests."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 86)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 140)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 165)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 176)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 188)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 197)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from AzureChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 208)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from AzureChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 217)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test invoke tokens from AzureChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_azure.py` (line 226)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test invoke tokens from AzureChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 163)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 219)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 227)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from ChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 239)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test invoke tokens from ChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 272)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 329)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/chat_models/test_base.py` (line 421)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from ChatOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 56)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 70)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 77)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 84)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 94)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 102)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 109)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from AzureOpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 150)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_azure.py` (line 173)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 14)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 22)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 30)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 39)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 50)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test batch tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 103)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 115)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 124)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 133)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 145)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 155)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 164)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test streaming tokens from OpenAI."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 208)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/integration_tests/llms/test_base.py` (line 233)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_azure.py` (line 239)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that max_completion_tokens can be used as a direct parameter."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_azure.py` (line 257)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that max_tokens is converted to max_completion_tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 536)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
{"id":"chatcmpl-9nhARrdUiJWEMd5plwV1Gc9NCjb9M","object":"chat.completion.chunk","created":1721631035,"model":"gpt-5.5","

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 1116)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that explicit total_tokens=0 is preserved, not replaced by sum."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3932)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Input tokens exceed the configured limit of 272000 tokens. Your messages "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3933)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"resulted in 300007 tokens. Please reduce the length of the messages."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3966)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "Input tokens exceed the configured limit" in str(exc_info.value)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3980)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "Input tokens exceed the configured limit" in str(exc_info.value)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 3994)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "Input tokens exceed the configured limit" in str(exc_info.value)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 4010)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "Input tokens exceed the configured limit" in str(exc_info.value)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 4024)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "Input tokens exceed the configured limit" in str(exc_info.value)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_base.py` (line 4053)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "Input tokens exceed the configured limit" in str(exc_info.value)

### [HIGH] Dangerous execution pattern: __import__ dynamic import

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_client_utils.py` (line 38)
- **Category:** dynamic_import
- **OWASP:** LLM07
__import__("sys").platform != "linux",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 29)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Minimal `_ChatGPTOAuthTokenProvider` for tests."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 110)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""The SDK-facing `api_key` must resolve to the provider's current token."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/chat_models/test_codex.py` (line 569)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""The `api_key` callable wired into the SDK must yield the access token."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/embeddings/test_base.py` (line 104)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that embeddings respect the 300k token per request limit."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 1)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Unit tests for `langchain_openai.chatgpt_oauth`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 274)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
assert "redirect_uri=http%3A%2F%2Flocalhost%3A1455%2Fauth%2Fcallback" in url

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 419)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "ChatGPT refresh token is no longer valid (`invalid_grant`)."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 558)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""End-to-end happy path using a stubbed callback + token endpoint."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 834)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
path="/auth/callback?code=abc&state=xyz",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 846)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
path="/auth/callback?error=access_denied&error_description=nope",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 853)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
path="/auth/callback?code=abc&state=xyz",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 865)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
path="/auth/callback?error=access_denied&error_description=user+declined",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 879)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
path="/auth/callback?error=invalid_scope",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 891)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"/auth/callback?error=oops&error_description="

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_chatgpt_oauth.py` (line 910)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
path="/auth/callback?error=access_denied&error_description=nope",

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_load.py` (line 12)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
llm = OpenAI(model="davinci", temperature=0.5, openai_api_key="hello", top_p=0.8)  # type: ignore[call-arg]

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openai/tests/unit_tests/test_load.py` (line 27)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
llm = OpenAI(model="davinci", temperature=0.5, openai_api_key="hello")  # type: ignore[call-arg]

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/langchain_openrouter/chat_models.py` (line 229)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Maximum number of completion tokens to generate."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/langchain_openrouter/chat_models.py` (line 424)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "OPENROUTER_API_KEY must be set."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 215)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that API key is read from OPENROUTER_API_KEY env var."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 224)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
with pytest.raises(ValueError, match="OPENROUTER_API_KEY must be set"):

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 260)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that ls_max_tokens is set when max_tokens is configured."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 1879)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that explicit total_tokens=0 is preserved, not replaced by sum."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 1891)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""prompt_tokens=0 must not fall through to input_tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 1902)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""completion_tokens=0 must not fall through to output_tokens."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2110)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that total_tokens is computed if not provided."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2147)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that zero-value token details are preserved (not dropped)."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2163)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test fallback to input_tokens/output_tokens key names."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/openrouter/tests/unit_tests/test_chat_models.py` (line 2470)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that max_completion_tokens is included when set."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 91)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Perplexity API key. Reads from `PPLX_API_KEY` or `PERPLEXITY_API_KEY`."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 111)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"Perplexity API key not provided. Pass `pplx_api_key` (or "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 112)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"`api_key`) to PerplexityEmbeddings, or set the `PPLX_API_KEY` "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/perplexity/langchain_perplexity/embeddings.py` (line 113)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"or `PERPLEXITY_API_KEY` environment variable."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/perplexity/tests/unit_tests/test_chat_models.py` (line 163)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test _create_usage_metadata with basic token counts."""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/perplexity/tests/unit_tests/test_embeddings.py` (line 45)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""`api_key=` should be accepted via populate_by_name alias."""

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 102)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = vector_store.similarity_search(

### [HIGH] RAG retrieval call with no visible sanitisation of retrieved content

- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 878)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = self.client.retrieve(self.collection_name, ids, with_payload=True)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/xai/langchain_xai/chat_models.py` (line 537)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"xAI API key is not set. Please set it in the `xai_api_key` field or "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/xai/langchain_xai/chat_models.py` (line 538)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"in the `XAI_API_KEY` environment variable."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/partners/xai/tests/unit_tests/test_chat_models.py` (line 37)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test that streaming correctly invokes on_llm_new_token callback."""

### [HIGH] Dangerous execution pattern: os.system() call

- **File:** `libs/standard-tests/langchain_tests/integration_tests/sandboxes.py` (line 1191)
- **Category:** os_system
- **OWASP:** LLM07
malicious_path = "'; import os; os.system('echo INJECTED'); #"

### [HIGH] Dangerous execution pattern: os.system() call

- **File:** `libs/standard-tests/langchain_tests/integration_tests/sandboxes.py` (line 1203)
- **Category:** os_system
- **OWASP:** LLM07
malicious_path = "'; import os; os.system('echo INJECTED'); #"

### [HIGH] LLM call with nearby user input and no visible sanitisation

- **File:** `libs/standard-tests/langchain_tests/integration_tests/tools.py` (line 32)
- **Category:** prompt_injection_likely
- **OWASP:** LLM01
result = tool.invoke(tool_call)

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/langchain_text_splitters/base.py` (line 259)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"This is needed in order to calculate max_tokens_for_prompt. "

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/langchain_text_splitters/base.py` (line 421)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Maximum number of tokens per chunk"""

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/langchain_text_splitters/base.py` (line 444)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "tokens_per_chunk must be greater than chunk_overlap"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/langchain_text_splitters/nltk.py` (line 47)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
msg = "When use_span_tokenize is True, separator should be ''"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/langchain_text_splitters/sentence_transformers.py` (line 71)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f" is: {self.maximum_tokens_per_chunk}."

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/langchain_text_splitters/sentence_transformers.py` (line 72)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
f" Argument tokens_per_chunk={self.tokens_per_chunk}"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/tests/integration_tests/test_nlp_text_splitters.py` (line 95)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
ValueError, match="When use_span_tokenize is True, separator should be ''"

### [HIGH] High-entropy string in a credential-like variable

- **File:** `libs/text-splitters/tests/integration_tests/test_text_splitter.py` (line 25)
- **Category:** possible_hardcoded_secret
- **OWASP:** LLM06
"""Test text splitter that uses a HuggingFace tokenizer."""

### [MEDIUM] RAG retrieval call — verify retrieved content is sanitised before LLM injection

- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 89)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = vector_store.similarity_search(query="thud", k=1)

### [MEDIUM] RAG retrieval call — verify retrieved content is sanitised before LLM injection

- **File:** `libs/core/langchain_core/vectorstores/in_memory.py` (line 104)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = vector_store.similarity_search(

### [MEDIUM] RAG retrieval call — verify retrieved content is sanitised before LLM injection

- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 235)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = vector_store.similarity_search(query="thud", k=1)

### [MEDIUM] RAG retrieval call — verify retrieved content is sanitised before LLM injection

- **File:** `libs/partners/chroma/langchain_chroma/vectorstores.py` (line 245)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = vector_store.similarity_search(

### [MEDIUM] RAG retrieval call — verify retrieved content is sanitised before LLM injection

- **File:** `libs/partners/qdrant/langchain_qdrant/qdrant.py` (line 124)
- **Category:** unsafe_rag
- **OWASP:** LLM01
results = vector_store.similarity_search(

### [LOW] LLM call near user input — sanitisation detected but verify it's sufficient

- **File:** `libs/langchain/langchain_classic/chains/flare/base.py` (line 217)
- **Category:** prompt_injection_possible
- **OWASP:** LLM01
self.response_chain.invoke(
