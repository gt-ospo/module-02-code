import math
from numbers import Real, Complex
from typing import Any

def my_abs(x : Any) -> Real:
    if isinstance(x, Real):
        if x < 0:
            return -x
        else:
            return x
    elif isinstance(x, Complex):
        return math.sqrt(x.real ** 2 + x.imag ** 2)
    else:
        return math.nan


def my_almost_eq(x : Any, y : Any) -> bool:
    return my_abs(x - y) < 1e-16
