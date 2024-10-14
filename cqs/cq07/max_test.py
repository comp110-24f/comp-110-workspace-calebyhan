"""Practicing with unit tests."""

__author__ = "730738108"

from find_max import find_and_remove_max

assert find_and_remove_max([1, 2, 3]) == 3

a = [1, 2, 3]
b = list(a)
find_and_remove_max(a)
assert a == b

assert find_and_remove_max([]) == -1
