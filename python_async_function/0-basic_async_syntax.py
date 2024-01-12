#!/usr/bin/env python3
"""
The basic async syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument,
    waits for a random delay and between 0 and max_delay seconds
    and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
