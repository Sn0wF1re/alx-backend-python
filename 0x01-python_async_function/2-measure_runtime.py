#!/usr/bin/env python3
"""
Creates function to measure total execution time
for wait_n(n, max_delay) and return total_time/n
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures average execution time for each task
    Args:
        n: number of times wait_random(max_delay) is spawned
        max_delay: maximum wait time between spawns
    Returns:
        Total_time/n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    return ((stop - start) / n)
