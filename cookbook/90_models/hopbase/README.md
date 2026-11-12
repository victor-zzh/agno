# HopBase Cookbook

This cookbook demonstrates how to use HopBase with the Agno framework. HopBase is an
OpenAI-compatible AI API gateway (`https://api.hop-base.com/v1`) that serves GPT, Claude,
Gemini and Grok models next to DeepSeek, GLM, Kimi and Qwen behind one base URL.

> **Prerequisites**: Fork and clone this repository if needed

## Quick Start

### 1. Create and activate a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Export your `HOPBASE_API_KEY`

Create an API key in the HopBase console (https://api.hop-base.com/login).

```shell
export HOPBASE_API_KEY=***
```

### 3. Install libraries

```shell
uv pip install -U openai agno
```

### 4. Run basic Agent

```shell
python cookbook/90_models/hopbase/basic.py
```

### 5. Run Agent with Tools

```shell
python cookbook/90_models/hopbase/tool_use.py
```

### 6. Run Agent that returns structured output

```shell
python cookbook/90_models/hopbase/structured_output.py
```

## Model Ids

The basic and tool examples use `glm-5.3`; the structured output example uses `gpt-6.1-sol`,
because how closely the output follows a JSON schema depends on the model. Other ids work with the same class, for example `gpt-6.1-sol`
or `claude-sonnet-5-5`:

```python
HopBase(id="gpt-6.1-sol")
```

The models a key can call depend on the groups attached to it. `GET /v1/models` returns
exactly those ids:

```shell
curl https://api.hop-base.com/v1/models -H "Authorization: Bearer $HOPBASE_API_KEY"
```

Notes:

- `glm-5.3` is a reasoning model. If you set `max_tokens`, leave room for reasoning
  (300 or more), otherwise the visible answer can be empty.
- `glm-5.3` does not accept image input. Use `gpt-6.1-sol` for image input.
- HopBase has no `/v1/embeddings` endpoint, so use a different embedder for knowledge bases.

## Resources & Support

### Official Links
- [Website](https://hop-base.com)
- [Documentation](https://hop-base.com/en/docs)
- [Models](https://hop-base.com/models)
- [Console](https://api.hop-base.com/login)

### API Reference
- **Base URL**: `https://api.hop-base.com/v1`
- **Models Endpoint**: `https://api.hop-base.com/v1/models`
