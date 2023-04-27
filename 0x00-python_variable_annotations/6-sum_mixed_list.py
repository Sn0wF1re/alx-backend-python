#!/usr/bin/env python3
"""
Creates a function sum_mixed_list
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """
    Takes a list of integers and floats and returns their sum as a float
    """
    sum = 0

    for i in mxd_lst:
        sum += i
    return sum
