#!/usr/bin/env python3
"""measure_runtime async function"""
import asyncio
import typing
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime of async_comprehension to run 4 time"""
    start: float = perf_counter()
    t1: asyncio.Task = asyncio.create_task(async_comprehension())
    t2: asyncio.Task = asyncio.create_task(async_comprehension())
    t3: asyncio.Task = asyncio.create_task(async_comprehension())
    t4: asyncio.Task = asyncio.create_task(async_comprehension())
    await asyncio.gather(t1, t2, t3, t4)
    end: float = perf_counter()
    return (end - start)
