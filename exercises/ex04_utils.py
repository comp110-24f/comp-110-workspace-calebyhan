"""EX04 - List Utility Functions."""

__author__: str = "730738108"


def all(lst: list[int], check: int) -> bool:
    """Check if all elements in a list are equal to a given integer.

    :param lst: a list of integers
    :param check: an integer to check against
    :return: a boolean
    """
    if len(lst) == 0:
        return False
    for i in lst:
        if i != check:
            return False
    return True


def max(lst: list[int]) -> int:
    """Find the maximum value in a list of integers.

    :param lst: a list of integers
    :return: an integer
    """
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")
    largest_int: int = lst[0]
    for i in lst:
        if i > largest_int:
            largest_int = i
    return largest_int


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Check if two lists of integers are equal.

    :param lst1: a list of integers
    :param lst2: a list of integers
    :return: a boolean
    """
    if len(lst1) != len(lst2):
        return False
    if len(lst1) > len(lst2):
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
    else:
        for i in range(len(lst2)):
            if lst1[i] != lst2[i]:
                return False
    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    """Combine two lists of integers.

    :param lst1: a list of integers
    :param lst2: a list of integers
    :return: a list of integers
    """
    for i in range(len(lst2)):
        lst1.append(lst2[i])
