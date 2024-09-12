"""Practice with Conditionals, Local Variables, and User Input"""

__author__: str = "730738108"


def guess_a_number() -> None:
    secret: int = 7
    number: int = int(input("Guess a number: "))
    print("Your guess was " + str(number))
    if number == secret:
        print("You got it!")
    elif number < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
