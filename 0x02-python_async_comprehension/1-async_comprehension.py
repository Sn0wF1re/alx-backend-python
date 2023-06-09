#!/usr/bin/env python3
"""
Write a coroutine called async_comprehension that takes no arguments
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns 10 random numbers from async generator() using list comprehension
    Args:
        None
    Returns:
        List of the random numbers
    """
    result = [i async for i in async_generator()]
    return result
