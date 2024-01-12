#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from typing import List
from asyncio import gather


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that executes multiple coroutines by calling 'task_wait_random'
    Args:
        n -> number of times to spawn 'task_wait_random'
        max_delay -> the number of seconds to wait before returning output
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    data_list = await gather(*tasks)
    new_list = []

    while data_list:
        minimum = data_list[0]  # arbitrary number in list
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    return new_list


if __name__ == "__main__":
    asyncio.run(task_wait_n)
