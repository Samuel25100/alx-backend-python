#!/usr/bin/env python3
"""make_multiplier takes a float multiplier return multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return function that take float arg and return mulitiplication"""

    def multiply(val: float) -> float:
        """take val and return multiplication of multiplier"""
        return val * multiplier
    return multiply
