#!/usr/bin/env python3
"""Spawn n number of wait_random function call"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """each call run concunrrently"""
    arr = []
    result = []
    for i in range(0, n):
        tk = asyncio.create_task(wait_random(max_delay))
        arr.append(tk)
    for i in asyncio.as_completed(arr):
        result.append(await i)
    return (result)
