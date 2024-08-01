#!/usr/bin/env python3
'''A module for sum_list:
    sums the values of a list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''A function sum_list
        Sums the values of a list of floats
        Returns: The sum of the elements of input_list
    '''
    sum: float = 0
    for value in input_list:
        sum += value
    return sum
