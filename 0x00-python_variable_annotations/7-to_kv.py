#!/usr/bin/env python3
'''A module for to_kv:
    Creats a tuple of string and square of int or float
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function to_kv:
        Creates a tuple of k and square of v
        Returns: tuple of k and v
    '''
    return (k, v ** 2)
