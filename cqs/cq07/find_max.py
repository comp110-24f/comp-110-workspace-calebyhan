"""Practicing with unit tests."""

__author__ = "730738108"


def find_and_remove_max(lst: list[int]) -> int:
    if len(lst) == 0:
        return -1
    largest = 0
    for item in lst:
        if item > largest:
            largest = item
    i: int = 0
    while i < len(lst):
        if lst[i] == largest:
            lst.pop(i)
        else:
            i += 1
    return largest
