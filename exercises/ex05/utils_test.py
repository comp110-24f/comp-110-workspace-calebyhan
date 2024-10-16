"""Testing util functions."""

__author__ = "730738108"

from utils import only_evens, sub, add_at_index


def test_only_evens() -> None:
    """Tests only_evens function."""
    assert only_evens([1, 2, 3]) == [2]
    assert only_evens([2, 3, 4]) == [2, 4]
    assert only_evens([]) == []
    return None


def test_sub() -> None:
    """Tests sub function."""
    assert sub([1, 2, 3], 0, 2) == [1, 2]
    assert sub([2, 3, 4], 1, 3) == [3, 4]
    assert sub([3, 4, 5], 5, 1) == []
    return None


def test_add_at_index() -> None:
    """Tests add_at_index function."""
    assert add_at_index([1, 2, 3], 4, 2) == [1, 2, 4, 3]
    assert add_at_index([2, 3, 4], 5, 1) == [2, 5, 3, 4]
    assert add_at_index([], 6, 0) == []
    return None
