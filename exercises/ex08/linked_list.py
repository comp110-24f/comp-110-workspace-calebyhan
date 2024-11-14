"""Linked Lists."""

from __future__ import annotations

__author__ = "730738108"


class Node:
    """Class for Node."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None = None) -> None:
        """Initialize Node.

        :param value: value of node
        :param next: next node
        """
        self.value = value
        self.next = next


def value_at(head: Node | None, index: int) -> int:
    """Value at index.

    :param head: Node to search
    :param index: index to search

    :return: value at index
    """
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    if index > 0:
        return value_at(head.next, index - 1)
    else:
        return head.value


def max(head: Node | None) -> int:
    """Max value.

    :param head: Node to search

    :return: max value
    """
    if head is None:
        raise ValueError("Cannot call max with None.")

    max_value = head.value
    if head.next is not None:
        next_max = max(head.next)
        if next_max > max_value:
            return next_max
        else:
            return max_value
    else:
        return max_value


def linkify(items: list[int]) -> Node | None:
    """Linkify a list.

    :param items: list to linkify

    :return: linked list
    """
    if len(items) == 0:
        return None

    head = Node(items[0])
    current = head
    for item in items[1:]:
        current.next = Node(item)
        current = current.next
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale linked list.

    :param head: Node to scale
    :param factor: factor to scale by

    :return: scaled linked list
    """
    if head is None:
        return None

    new_head = Node(head.value * factor)
    new_head.next = scale(head.next, factor)
    return new_head
