"""Practice with While Loops over a String"""

__author__: str = "730738108"


def num_instances(phrase: str, search_char: str) -> int:
    """
    Counts number of instances of search_char in phrase with a while loop

    :param phrase: the phrase to parse through
    :param search_char: the character to count instances in phrase
    """
    count: int = 0
    i: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1

    return count
