#!/usr/bin/env python3
'''async_comprehensions module:
    comphension of async generator
'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''async_comprehension:
        returns a list comprehension of async_generator
    '''
    return [i async for i in async_generator()]
