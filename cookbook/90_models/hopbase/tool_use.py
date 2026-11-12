"""
HopBase Tool Use
================

Cookbook example for `hopbase/tool_use.py`.
"""

import asyncio

from agno.agent import Agent
from agno.models.hopbase import HopBase

# ---------------------------------------------------------------------------
# Create Agent
# ---------------------------------------------------------------------------


def get_order_status(order_id: str) -> str:
    """Look up the shipping status of an order.

    Args:
        order_id: The order id, for example "A-1042".
    """
    statuses = {"A-1042": "shipped", "A-1043": "processing"}
    return statuses.get(order_id, "not found")


agent = Agent(
    model=HopBase(id="glm-5.3"),
    tools=[get_order_status],
    markdown=True,
)


async def run_async():
    # --- Async ---
    await agent.aprint_response("Check orders A-1042 and A-1043.")

    # --- Async + Streaming ---
    await agent.aprint_response("What is the status of order A-9999?", stream=True)


# ---------------------------------------------------------------------------
# Run Agent
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # --- Sync ---
    agent.print_response("What is the status of order A-1042?")

    # --- Sync + Streaming ---
    agent.print_response("Is order A-1043 shipped yet?", stream=True)

    # --- Async and Async + Streaming ---
    # Run both async calls in one event loop: the model caches its async client,
    # and a client created in one asyncio.run() loop cannot be reused in another.
    asyncio.run(run_async())
