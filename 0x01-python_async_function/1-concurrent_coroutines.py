#!/usr/bin/env python3
"""Spawn n number of wait_random function call"""
import asyncio
from typing import List, Any
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """each call run concunrrently"""
    arr: List[asyncio.Task] = []
    result: List[float] = []
    for i in range(0, n):
        arr.append(asyncio.create_task(wait_random(max_delay)))
    for val in asyncio.as_completed(arr):
        result.append(await val)
    return (result)
