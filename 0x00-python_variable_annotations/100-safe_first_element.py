#!/usr/bin/env python3
"""
Creates function safe_first_element
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args: lst
    Return: Any type or None
    """
    if lst:
        return lst[0]
    else:
        return None
