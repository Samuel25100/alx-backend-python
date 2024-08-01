#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return list of iterable value and int"""
    return [(i, len(i)) for i in lst]
