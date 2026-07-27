"""Intentionally vulnerable AI app — used as scanner test fixture."""
import openai

# LLM06 - hardcoded secret
openai.api_key = "sk-proj-aB3dEfGhIjKlMnOpQrStUvWxYz1234567890"

def handle_chat(user_message):
    # LLM01 - user input flows directly into LLM call
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}]
    )
    # LLM07 - LLM output passed to eval()
    return eval(response.choices[0].message.content)