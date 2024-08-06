#!/usr/bin/env python3
"""async_generator function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """asynchronously wait 1 second, then yield a random number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
