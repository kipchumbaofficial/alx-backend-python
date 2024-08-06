#!/usr/bin/env python3
'''async_generator module
    asynchronous generator
'''
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    '''async_generator:
        yields a random number betwn 0 and 10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
