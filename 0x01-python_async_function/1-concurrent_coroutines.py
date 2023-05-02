#!/usr/bin/env python3
"""
Create a coroutine wait_n that spawns wait_random n times
with a given max_delay
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: number of times wait_random is spawned
        max_delay: max delay for the wait_random function
    Return: List of all delays
    """
    taskList = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return await asyncio.gather(*taskList)
