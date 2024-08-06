#!/usr/bin/env python3
"""async_comprehension function"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Using async comprehension return list from async generator"""
    val: List[float] = [i async for i in async_generator()]
    return val
