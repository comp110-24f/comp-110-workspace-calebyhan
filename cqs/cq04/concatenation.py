"""Practice with Importing + Scope"""

__author__: str = "730738108"


def concat(word1: str, word2: str) -> str:

    return word1 + word2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1=word1, word2=word2))
