#!/usr/bin/env python3
"""
"""
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Args:
        dct: Mapping
        key: Any
        default: TypeVar or None
    Return: Any or TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
