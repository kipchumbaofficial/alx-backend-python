#!/usr/bin/env python3
'''wait_random module:
    Delays for a random time
'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''wait_random
        Returns delay time
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
