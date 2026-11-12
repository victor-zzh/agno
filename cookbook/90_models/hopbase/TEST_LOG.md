# HopBase Tests

Run against the live HopBase API with Python 3.12 and openai 3.49.0.

### basic.py

**Status:** PASS

**Description:** Basic HopBase cookbook (`glm-5.3`) covering sync, streaming, async, and async streaming agent responses.

**Result:** All four responses printed, no errors.

---

### tool_use.py

**Status:** PASS

**Description:** Agent (`glm-5.3`) with a Python function tool (`get_order_status`) covering sync, streaming, async, and async streaming tool calls.

**Result:** The model called `get_order_status` in all four runs (both orders in the "A-1042 and A-1043" prompt) and answered from the tool result, including the "not found" case.

---

### structured_output.py

**Status:** PASS

**Description:** Agent (`gpt-6.1-sol`) with `output_schema=MovieScript` prompted with "New York".

**Result:** `run.content` is a populated `MovieScript` instance.

---

### Other checks

- String syntax `Agent(model="hopbase:glm-5.3")` resolves to `HopBase` and returns a response.
- Tool calling (sync and streaming) and `output_schema` also pass on `gpt-6.1-sol`; `output_schema` passes on `claude-sonnet-5-5`.
- `output_schema` on `glm-5.3` did not return a valid object in testing, so the structured output example uses `gpt-6.1-sol`.
- Image input works on `gpt-6.1-sol`. `glm-5.3` rejects images with a 400 error that names the model.

### Unit tests

`libs/agno/tests/unit/models/test_hopbase.py`: 8 passed, without network access.
