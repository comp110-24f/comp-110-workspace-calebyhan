def get_first(lst: list[int]) -> int:
    return lst[0]

def remove_first(lst: list[int]) -> None:
    lst.pop(0)

def get_and_remove_first(lst: list[int]) -> int:
    first: int = get_first(lst)
    remove_first(lst)
    return first
