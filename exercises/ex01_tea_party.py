"""Tea party exercise"""

__author__: str = "730738108"


def main_planner(guests: int) -> None:
    """
    Combining all helper functions below for user output

    :param guests: the number of guests attending the tea party
    """
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """
    Calculate number of tea bags required for the party

    :param people: the number of guests attending the tea party
    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculate number of treats required for the party

    :param people: the number of guests attending the tea party
    """
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculate cost of party

    :param tea_count: the number of tea bags needed
    :param treat_count: the number of treats needed
    """
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
