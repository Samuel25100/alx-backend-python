#!/usr/bin/env python3
"""Return random number between given val and 0"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Val is going to be used for .sleep() input"""
    val: float = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
