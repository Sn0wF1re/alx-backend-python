#!/usr/bin/env python3
"""
Write a coroutine that takes no arguments
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    Args:
        None
    Returns:
        A generator iterator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
