#!/usr/bin/env python3
'''A module for element_length:
    Create a tuple of a Sequence and its length
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''A function element_length:
        Returns: a tuple of sequence and its length
    '''
    return [(i, len(i)) for i in lst]
