#!/usr/bin/env python3
'''A module for  safe_first_element:
    gives first elemnt of a list
'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''A function  safe_first_element:
        Returns: first elemnt of lst or None
    '''
    if lst:
        return lst[0]
    else:
        return None
