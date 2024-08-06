#!/usr/bin/env python3
'''measure_time modules:
    measures run time of wait_n
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure_time:
        Returns elapsed timed on running wait_n
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time: float = end_time - start_time
    elapsed_time = total_time / n
    return elapsed_time
