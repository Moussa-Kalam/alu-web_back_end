#!/usr/bin/env python3
"""
Complex-types annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that takes a list of floats and
    returns their sum as a float
    """
    return sum(input_list)
