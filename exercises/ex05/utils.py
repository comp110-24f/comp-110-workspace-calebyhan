"""Building util functions to test."""

__author__ = "730738108"

def only_evens(lst: list[int]) -> list[int]:
    """Returns a list of only the even numbers in a list.
    
    :param lst: a list of integers
    :return: a list of only the even numbers in the list
    """
    ret: list[int] = []
    for item in lst:
        # check if the item is even then add it to the list
        if item % 2 == 0:
            ret.append(item)
    return ret


def sub(lst: list[int], a: int, b: int) -> list[int]:
    """Returns a list of integers from a list between two indices.
    
    :param lst: a list of integers
    :param a: an integer
    :param b: an integer
    :return: a list of integers between the two indices
    """
    ret: list[int] = []

    # check if the indices are out of bounds
    if a < 0:
        a = 0
    if b > len(lst):
        b = len(lst)
    if a > len(lst) or b < 0:
        return ret

    # add the elements between the indices to the list
    i: int = a
    while i < b:
        ret.append(lst[i])
        i += 1
    return ret


def add_at_index(lst: list[int], a: int, b: int) -> None:
    """Returns a list of integers with a number added at a specific index.
    
    :param lst: a list of integers
    :param a: an integer
    :param b: an index to add the integer
    :return: a list of integers with the number added at the index
    """
    # check if the index is out of bounds
    if len(lst) < b or b < 0:
        raise IndexError("Index is out of bounds for the input list")

    # check if the list is empty
    if len(lst) == 0:
        lst.append(a)
        return None

    # create buffer space
    lst.append(0)
    
    # shift elements to the right
    i: int = len(lst) - 1
    while i > b:
        lst[i] = lst[i - 1]
        i -= 1
    
    # insert the new element
    lst[b] = a
    