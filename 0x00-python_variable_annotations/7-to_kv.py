#!/usr/bin/env python3
"""to_kv takes a string k and an int/float v and returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple of k string and square of v in float"""
    result = []
    result.append(k)
    result.append(v ** 2)
    return tuple(result)
