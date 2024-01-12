#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather
    """
    p = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - p
    return elapsed


if __name__ == " __main__":
    asyncio.run(measure_runtime())
