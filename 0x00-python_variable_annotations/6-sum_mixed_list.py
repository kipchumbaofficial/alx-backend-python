#!/usr/bin/env python3
'''A module for sum_mixed_list:
    sums a list of integers and floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''A function sum_mixed_list:
        sums elements of mxd_lst
        Returns: sum of the elements of mxd_list
    '''
    sum: float = 0
    for value in mxd_lst:
        sum += value
    return sum
