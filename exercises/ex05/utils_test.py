"""Testing util functions."""

__author__ = "730738108"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_1() -> None:
    """Tests only_evens function."""
    assert only_evens([1, 2, 3]) == [2]
    return None


def test_only_evens_2() -> None:
    """Tests only_evens function."""
    assert only_evens([2, 3, 4]) == [2, 4]
    return None


def test_only_evens31() -> None:
    """Tests only_evens function."""
    assert only_evens([]) == []
    return None


def test_sub_1() -> None:
    """Tests sub function."""
    assert sub([1, 2, 3], 0, 2) == [1, 2]
    return None


def test_sub_2() -> None:
    """Tests sub function."""
    assert sub([2, 3, 4], 1, 3) == [3, 4]
    return None


def test_sub_3() -> None:
    """Tests sub function."""
    assert sub([3, 4, 5], 5, 1) == []
    return None


def test_add_at_index_1() -> None:
    """Tests add_at_index function."""
    x: list[int] = [1, 2, 3]
    assert add_at_index(x, 4, 2) is None
    return None


def test_add_at_index_2() -> None:
    """Tests add_at_index function."""
    y: list[int] = [2, 3, 4]
    add_at_index(y, 5, 1)
    assert y == [2, 5, 3, 4]
    return None


def test_add_at_index_3() -> None:
    """Tests add_at_index function."""
    with pytest.raises(IndexError):
        z: list[int] = [1, 2, 3]
        add_at_index(z, 4, 5)
        assert z == [1, 2, 3]
    return None
