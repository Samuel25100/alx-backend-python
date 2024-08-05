#!/usr/bin/env python3
"""Contain function named measure_time return float"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the time its take to run function wait_n"""
    start: float = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = perf_counter()
    return ((end - start) / n)
