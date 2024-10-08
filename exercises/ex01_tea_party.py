"""Tea party exercise"""

__author__: str = "730738108"


def main_planner(guests: int) -> None:
    """
    Combining all helper functions below for user output

    :param guests: the number of guests attending the tea party
    """
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # prints out all output needed for this exercise, calling all functions defined
    # below


def tea_bags(people: int) -> int:
    """
    Calculate number of tea bags required for the party

    :param people: the number of guests attending the tea party
    """
    return people * 2
    # returns a weighted value for tea_bags


def treats(people: int) -> int:
    """
    Calculate number of treats required for the party

    :param people: the number of guests attending the tea party
    """
    return int(tea_bags(people=people) * 1.5)
    # calls tea_bags to determine how many treats are needed based off of how many
    # people there are


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculate cost of party

    :param tea_count: the number of tea bags needed
    :param treat_count: the number of treats needed
    """
    return tea_count * 0.5 + treat_count * 0.75
    # returns a weighted value for both tea_count and treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # calls the main function that runs all the code, and uses user input as an argument
