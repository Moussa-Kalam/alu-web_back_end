#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
     Function that takes a float multiplier as argument
    returns a function that multiplies a float by multiplier.
    """

    def fn(n: float) -> float:
        """Multiply a float by a multiplier"""
        return n * multiplier

    return fn
