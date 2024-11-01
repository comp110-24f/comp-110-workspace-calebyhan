"""File to define Fish class."""

__author__: str = "730738108"


class Fish:
    """Class definition for Fish."""

    def __init__(self):
        """Constructor for class Fish."""
        self.age: int = 0

    def one_day(self) -> None:
        """Changing attributes of a fish for each day.

        :return: None
        """
        self.age += 1
        return None
