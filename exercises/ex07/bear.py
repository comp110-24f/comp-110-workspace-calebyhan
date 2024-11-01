"""File to define Bear class."""

__author__: str = "730738108"


class Bear:
    """Class definition for Bear."""

    def __init__(self):
        """Constructor for class Bear."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """Changing attributes of a bear for each day.

        :return: None
        """
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Changing hunger score for number of fish eaten.

        :param num_fish: Number of fish eaten

        :return: None
        """
        self.hunger_score += num_fish
        return None
