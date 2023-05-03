#!/usr/bin/env python3
"""
Write a measure_runtime coroutine
that will execute async_comprehension four times
in parallel using asyncio.gather
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures total runtime
    Args:
        None
    Returns:
        total runtime
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start
