#!/usr/bin/env python3
"""
Create function to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: str
        v: int or float
    Returns: Tuple whose first element is string k
            and second element is the square of the int/float
    """
    return tuple([k, v**2])
