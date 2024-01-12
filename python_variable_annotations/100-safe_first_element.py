#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""
from typing import Union, Sequence, Any


# The types of the elements of the input were not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """First element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
