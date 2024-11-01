"""File to define River class."""

__author__: str = "730738108"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class definition for River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears.

        :param num_fish: Number of fish in river.
        :param num_beras: Number of bears in river.
        """
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Make sure that the ages of the animals are under certain thresholds.

        :return: None
        """
        rem_fish: list[Fish] = []
        rem_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                rem_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                rem_bears.append(bear)
        self.fish = list(rem_fish)
        self.bears = list(rem_bears)
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove certain number of fishes.

        :param amount: Number of fish to remove.

        :return: None
        """
        rem_fish: list[Fish] = []
        for i in range(amount, len(self.fish)):
            rem_fish.append(self.fish[i])
        self.fish = list(rem_fish)
        return None

    def bears_eating(self) -> None:
        """Have the bears eat.

        :return: None
        """
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self) -> None:
        """Check that bears are not dying of hunger.

        :return: None
        """
        rem_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                rem_bears.append(bear)
        self.bears = list(rem_bears)
        return None

    def repopulate_fish(self) -> None:
        """Repopulate the fish.

        :return: None
        """
        for _ in range(len(self.fish) // 2 * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Repopulate the bears.

        :return: None
        """
        for _ in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Output for river information.

        :return: None
        """
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river.

        :return: None
        """
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Call one_river_day 7 times.

        :return: None
        """
        for _ in range(7):
            self.one_river_day()
