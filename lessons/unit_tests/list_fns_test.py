from list_fns import get_first, get_and_remove_first, remove_first


def test_get_first() -> None:
    assert get_first([1, 2, 3]) == 1
    assert get_first([2, 3, 4]) == 2
    assert get_first([3, 4, 5]) == 3


def test_remove_first() -> None:
    lst: list[int] = [1, 2, 3]
    remove_first(lst)
    assert lst == [2, 3]

    lst = [2, 3, 4]
    remove_first(lst)
    assert lst == [3, 4]

    lst = [3, 4, 5]
    remove_first(lst)
    assert lst == [4, 5]


def test_get_and_remove_first() -> None:
    lst: list[int] = [1, 2, 3]
    assert get_and_remove_first(lst) == 1
    assert lst == [2, 3]

    lst = [2, 3, 4]
    assert get_and_remove_first(lst) == 2
    assert lst == [3, 4]

    lst = [3, 4, 5]
    assert get_and_remove_first(lst) == 3
    assert lst == [4, 5]


test_get_first()
test_remove_first()
test_get_and_remove_first()
