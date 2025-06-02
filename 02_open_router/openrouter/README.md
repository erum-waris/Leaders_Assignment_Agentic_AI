
# Explore-UV with OpenRouter & OpenAI Agents SDK

This project demonstrates how to use `uv` for managing Python environments and how to integrate the OpenRouter API with OpenAI Agents SDK to communicate with LLMs like Gemini and DeepSeek.

---

## 🚀 Getting Started

### 1. Install & Initialize `uv`

```bash
uv version
uv help
uv init --package openrouter
cd openrouter
code .
```

### 2. Create and Activate Virtual Environment

```bash
uv venv
source .venv/bin/activate  # On Linux/macOS
.\.venv\Scripts\activate   # On Windows
```

Then, select the recommended Python interpreter `.venv/bin/python` in VSCode.

---

## 🔑 Setup for OpenRouter

1. Sign up at [https://openrouter.ai](https://openrouter.ai)
2. Get your **OpenRouter API Key**
3. Choose a free model (e.g., Gemini, DeepSeek)

> Free models allow 20 requests/minute and 200 requests/day.

List of models: https://openrouter.ai/models

---

## 📦 Installation

Install the required SDK:

```python
!pip install -Uq openai-agents
```

Also include:

```python
import nest_asyncio
nest_asyncio.apply()
```

---

## 🔐 API Configuration

```python
from google.colab import userdata

OPENROUTER_API_KEY = userdata.get("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free"
```

---

## 💬 Using OpenRouter API

```python
import requests
import json

response = requests.post(
  url=f"{BASE_URL}/chat/completions",
  headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
  data=json.dumps({
    "model": MODEL,
    "messages": [{"role": "user", "content": "What is the meaning of life?"}]
  })
)

data = response.json()
print(data['choices'][0]['message']['content'])
```

---

## 🤖 Using OpenAI Agents SDK

```python
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

client = AsyncOpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)
set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )
    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## ⚠️ Common Errors & Fixes

### ❌ 404 - No Endpoints Found

**Cause:** Prompt training is disabled.

**Fix:**
1. Go to [OpenRouter Privacy Settings](https://openrouter.ai/settings/privacy)
2. Enable `Prompt Training`

---

## ✅ Conclusion

You can now integrate powerful LLMs into your Python projects easily using OpenRouter and OpenAI Agents SDK. Have fun exploring AI with `uv`!

-