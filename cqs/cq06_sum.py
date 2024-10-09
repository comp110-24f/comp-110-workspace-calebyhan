"""Summing the elements of a list using different loops"""

__author__: str = "730738108"


def w_sum(vals: list[float]) -> float:
    i: int = 0
    sum_list: float = 0
    while i < len(vals):
        sum_list += vals[i]
        i += 1
    return sum_list


def f_sum(vals: list[float]) -> float:
    sum_list: float = 0
    for val in vals:
        sum_list += val
    return sum_list


def f_range_sum(vals: list[float]) -> float:
    sum_list: float = 0
    for i in range(len(vals)):
        sum_list += vals[i]
    return sum_list
