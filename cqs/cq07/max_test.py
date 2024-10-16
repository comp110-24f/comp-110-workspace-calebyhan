"""Practicing with unit tests."""

__author__ = "730738108"

from find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    assert find_and_remove_max([1, 2, 3]) == 3

    a = [1, 8, 2, 3, 3]
    find_and_remove_max(a)
    assert a == [1, 2, 3, 3]

    assert find_and_remove_max([]) == -1


test_find_and_remove_max()
