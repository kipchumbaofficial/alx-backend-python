#!/usr/bin/env python3
'''A module for zoom_array:
    Create a List from a tuple
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''function zoom_array:
        creates a list from tuple with factor number of elements
        Returns: A list with factor number of elemnets fro, lst
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
