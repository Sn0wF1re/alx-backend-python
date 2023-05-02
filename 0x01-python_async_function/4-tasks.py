#!/usr/bin/env python3
"""
Take code from wait_n() but call task_wait_random()
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n: number of times wait_random is spawned
        max_delay: max delay for the wait_random function
    Return: List of all delays
    """
    taskList = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(taskList)]
