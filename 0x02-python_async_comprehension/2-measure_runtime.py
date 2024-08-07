#!/usr/bin/env python3
'''measure_runtime module:
    measures run time
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure runtime function:
        returns runtime
    '''
    tasks = [async_comprehension() for _ in range(4)]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()

    return (end_time - start_time)
