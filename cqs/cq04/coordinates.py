"""Practice with Importing + Scope"""

__author__: str = "730738108"


def get_coords(xs: str, ys: str) -> None:
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1
        i += 1
