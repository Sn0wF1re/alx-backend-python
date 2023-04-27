#!/usr/bin/env python3
"""
Creates a function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args: multiplier(float)
    Returns: function that multiplies a float by multiplier
    """
    def multiplier_func(x: float) -> float:
        """
        multiplier times x
        """
        return multiplier * x
    return multiplier_func
