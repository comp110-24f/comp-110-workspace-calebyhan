"""Practicing with dictionary functions."""

__author__ = "730738108"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary.

    :param input_dict: A dictionary to invert.

    :return: A dictionary with the keys and values of the input dictionary inverted."""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        # check for duplicate keys
        if input_dict[key] in inverted_dict:
            raise KeyError("Duplicate key found.")

        # add the key/value pair to the inverted dictionary
        inverted_dict[input_dict[key]] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently.

    :param input_dict: A dictionary of names and favorite colors.
    :return: The color that appears most frequently."""
    colors: dict[str, int] = {}

    # count the number of times each color appears
    for key in input_dict:
        if input_dict[key] in colors:
            colors[input_dict[key]] += 1
        else:
            colors[input_dict[key]] = 1

    # find the color that appears most frequently
    max_color: str = ""
    max_count: int = 0
    for key in colors:
        if colors[key] > max_count:
            max_color = key
            max_count = colors[key]
    return max_color


def count(lst: list[str]) -> dict[str, int]:
    """Counts the number of times each value appears in a list.

    :param input_dict: A list of values.

    :return: A dictionary of the number of times each value appears."""
    counts: dict[str, int] = {}
    for item in lst:
        # check if the item is already in the dictionary
        if item in counts:
            counts[item] += 1
        # add the item to the dictionary if it is not already there
        else:
            counts[item] = 1
    return counts


def alphabetizer(lst: list[str]) -> dict[str, list[str]]:
    """Alphebetizes a list of strings by the first letter.

    :param lst: A list of strings.

    :return: A dictionary of strings alphabetized by the first letter."""
    ret: dict[str, list[str]] = {}
    for item in lst:
        # check if the first letter is already in the dictionary
        if item[0].lower() in ret:
            ret[item[0].lower()].append(item)
        # add the first letter to the dictionary if it is not already there
        else:
            ret[item[0].lower()] = [item]
    return ret


def update_attendance(input_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance record of a student.

    :param input_dict: A dictionary of attendance records.
    :param day: The day of the attendance record.
    :param student: The student to update.

    :return: None"""
    # check if the day or student is already in the dictionary
    if day in input_dict and student not in input_dict[day]:
        input_dict[day].append(student)
    else:
        input_dict[day] = [student]
    return None
