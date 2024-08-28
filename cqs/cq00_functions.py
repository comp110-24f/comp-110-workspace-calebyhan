"""Functions Challenge"""

__author__: str = "730738108"


def mimic(message: str) -> str:
    """
    Returns the inputted message

    :param message: message to mimic back
    """
    return message


def main() -> None:
    """
    Returns the output of the mimic function
    """
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
