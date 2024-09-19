"""EX03 - Wordle - Implementation of Wordle."""

__author__: str = "730738108"


def input_guess(secret_word_len: int) -> str:
    """
    Gets the user input for their word guess.

    :param secret_word_len: Length of the secret word we are trying to guess
    """
    guess: str = input("Enter a " + str(secret_word_len) + " character word: ")

    # if the guess is the right length, return it. otherwise, loop until valid
    if len(guess) == secret_word_len:
        return guess
    while True:
        guess: str = input(
            "That wasn't " + str(secret_word_len) + " chars! Try again: "
        )
        if len(guess) == secret_word_len:
            return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """
    Checks if the character guess is in the secret word.

    :param word:
    :param search_char:
    """
    # check that the character guess is length 1
    assert len(char_guess) == 1

    # check if the character is in the word
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """
    Outputs the emoji string given the secret word and the guess.

    :param guess:
    :param secret_wrrd
    """
    # check that the guess and the secret word are the same length
    assert len(guess) == len(secret_word)

    # emoji constants
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    ret: str = ""
    i: int = 0
    while i < len(guess):
        # check if the letters in the same position match
        if guess[i] == secret_word[i]:
            ret += GREEN_BOX

        # else, check if the character is in the word. if so: yellow, if not: white
        else:
            in_word: bool = contains_char(secret_word=secret_word, char_guess=guess[i])
            if in_word:
                ret += YELLOW_BOX
            else:
                ret += WHITE_BOX

        # increment index counter
        i += 1
    return ret


def main(secret: str) -> None:
    """
    The main function that takes in the secret word and plays the wordle game.

    :param secret:
    """
    turn: int = 1
    while True:
        # print turn number
        print("=== Turn " + str(turn) + "/6 ===")

        # get user guess and output the result
        guess: str = input_guess(len(secret))
        print(emojified(guess=guess, secret_word=secret))

        # if the user won, then exit the game
        if guess == secret:
            print("You won in " + str(turn) + " turns!")
            quit()

        # increment the turn counter
        turn += 1
    # the main function to run the wordle game


if __name__ == "__main__":
    main(secret="codes")
    # calls the main function that runs all the code
