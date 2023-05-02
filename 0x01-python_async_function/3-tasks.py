#!/usr/bin/env python3
"""
Create a function that takes an integer, max_delay
and returns a asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay: max wait time
    Returns:
        asyncio.Task object
    """
    return asyncio.Task(wait_random(max_delay))
