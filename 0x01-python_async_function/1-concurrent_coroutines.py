#!/usr/bin/env python3
'''wait_n module:
    spawns wait_random given number of times
'''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''wait_n:
        Returns a list of delay times
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    retVal: List[float] = await asyncio.gather(*tasks)
    return retVal
