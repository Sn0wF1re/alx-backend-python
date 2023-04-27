#!/usr/bin/env python3
"""
Creates a function element_length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args: lst
    Return: a list of a tuple containing a sequence and int
    """
    return [(i, len(i)) for i in lst]
