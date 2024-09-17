"""Practice with While Loops over a String"""

__author__: str = "730738108"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    i: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1

    return count
