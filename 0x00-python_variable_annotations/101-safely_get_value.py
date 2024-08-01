#!/usr/bin/env python3
'''Module for safely_get_value:
    Safely gets value of a Mapping
'''
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''Function safely_get_value:
        Returns: a value of key in dct or None
    '''
    if key in dct:
        return dct[key]
    else:
        return default
