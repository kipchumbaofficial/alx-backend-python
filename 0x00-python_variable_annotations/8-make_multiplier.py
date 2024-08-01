#!/usr/bin/env python3
'''A module for make_multiplier:
    Makes a multiplier for a given number
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''A function make_multiplier
        makes multiplier for the given number
        Returns: Multiplier function of give number
    '''
    def product(new_num: float) -> float:
        '''A function product:
            multiplier function
            Returns: multiplier * new_num
        '''
        return multiplier * new_num
    return product
