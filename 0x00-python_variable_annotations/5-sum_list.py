#!/usr/bin/env python3
"""sum_list takes a list of floats as argument and returns their sum"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return float type"""
    val = 0.0
    for i in input_list:
        val += i
    return val
