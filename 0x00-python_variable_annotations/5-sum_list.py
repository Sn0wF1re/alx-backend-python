#!/usr/bin/env python3
"""
Create a function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of inputs and returns their sum as a float
    """
    sum = 0

    for i in input_list:
        sum += i
    return sum
