"""
HopBase Basic
=============

Cookbook example for HopBase, OpenAILike model provider.
"""

import asyncio

from agno.agent import Agent
from agno.models.hopbase import HopBase

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------

agent = Agent(model=HopBase(id="glm-5.3"), markdown=True)

# You can also select the provider by string, which resolves to the same class:
# agent = Agent(model="hopbase:glm-5.3", markdown=True)

# The same base URL serves other model families. Swap the id to change models:
# agent = Agent(model=HopBase(id="gpt-6.1-sol"), markdown=True)
# agent = Agent(model=HopBase(id="claude-sonnet-5-5"), markdown=True)


async def run_async():
    # --- Async ---
    await agent.aprint_response("Share a 2 sentence horror story")

    # --- Async + Streaming ---
    await agent.aprint_response(
        "Write a short poem about artificial intelligence", stream=True
    )


# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("Explain quantum computing in simple terms")

    # --- Sync + Streaming ---
    agent.print_response("Explain quantum computing in simple terms", stream=True)

    # --- Async and Async + Streaming ---
    # Run both async calls in one event loop: the model caches its async client,
    # and a client created in one asyncio.run() loop cannot be reused in another.
    asyncio.run(run_async())
