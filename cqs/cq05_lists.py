"""Mutating functions."""

__author__: str = "730738108"


def manual_append(input_list: list[int], add_value: int) -> None:
    """
    Append a value to a list.

    :param input_list: a list of integers
    :param add_value: an integer to add to the list
    :return: None
    """
    input_list.append(add_value)


def double(input_list: list[int]) -> None:
    """
    Double the values in a list.

    :param input_list: a list of integers
    :return: None
    """
    i: int = 0
    while i < len(input_list):
        input_list[i] = input_list[i] * 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(input_list=list_2)

print(list_1)
print(list_2)
