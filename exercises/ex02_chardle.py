"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730738108"


def input_word() -> str:
    """
    Takes in a word as input and checks if it is 5 characters long. If it is not, then
    exits the program. Returns the word if it is.
    """
    word = input("Enter a 5-character word: ")

    # check if the word is a valid length, if not then exit
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()

    return word


def input_letter() -> str:
    """
    Takes in a character as input and checks if it is 1 characters long. If it is not,
    then exits the program. Returns the character if it is.
    """
    letter = input("Enter a single character: ")

    # check if the character is a valid length, if not then exit
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return letter


def contains_char(word: str, letter: str) -> None:
    """
    Counts all occurences of the letter in the word one by one by checking the indices
    and increments a counter when found. Customizes the output depending on how many
    occurences there are.

    :param word: The word to search
    :param letter: The letter to search in the word
    """
    # counter for how many of a letter is in a word
    count: int = 0

    print("Searching for " + letter + " in " + word)

    # checking one by one index if letter is in the word
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    # customized output depending on the value of count
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """
    Function to run the entire program.
    """
    contains_char(word=input_word(), letter=input_letter())
    # the main function to call contains_char


if __name__ == "__main__":
    main()
    # calls the main function that runs all the code
