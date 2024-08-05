#!/usr/bin/env python3
"""contain function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return list of each output"""
    arr: List[asyncio.Task] = []
    result: List[float] = []
    for i in range(0, n):
        arr.append(task_wait_random(max_delay))
    for val in asyncio.as_completed(arr):
        result.append(await val)
    return (result)
