"""EX04 - List Utility Functions."""

__author__: str = "730738108"


def all(lst: list[int], check: int) -> bool:
    """Check if all elements in a list are equal to a given integer.

    :param lst: a list of integers
    :param check: an integer to check against
    :return: a boolean
    """
    # check if the list is empty
    if len(lst) == 0:
        return False

    # check if all elements in the list are equal to the given integer
    i: int = 0
    while i < len(lst):
        # exit early if the current element is not equal to the given integer
        if lst[i] != check:
            return False
        i += 1
    return True


def max(lst: list[int]) -> int:
    """Find the maximum value in a list of integers.

    :param lst: a list of integers
    :return: an integer
    """
    # check if the list is empty
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")

    # find the maximum value in the list
    largest_int: int = lst[0]
    i: int = 0
    while i < len(lst):
        # update the largest integer if the current element is greater
        if lst[i] > largest_int:
            largest_int = lst[i]
        i += 1
    return largest_int


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Check if two lists of integers are equal.

    :param lst1: a list of integers
    :param lst2: a list of integers
    :return: a boolean
    """
    # check if the lists are the same length
    if len(lst1) != len(lst2):
        return False

    # check which list is longer
    i: int = 0
    if len(lst1) > len(lst2):
        while i < len(lst2):
            # exit early if the current elements are not equal
            if lst1[i] != lst2[i]:
                return False
            i += 1
    else:
        while i < len(lst1):
            # exit early if the current elements are not equal
            if lst1[i] != lst2[i]:
                return False
            i += 1
    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    """Combine two lists of integers.

    :param lst1: a list of integers
    :param lst2: a list of integers
    :return: a list of integers
    """
    # add the elements of the second list to the first list
    i: int = 0
    while i < len(lst2):
        lst1.append(lst2[i])
        i += 1
