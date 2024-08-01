#!/usr/bin/env python3
"""sum_mixed_list takes a list of integers and floats and returns their sum."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return float type."""
    val: float = 0.0
    for i in mxd_lst:
        val += i
    return val
