from __future__ import annotations

"""Making a singly-linked list data structure."""

__author__ = "730580318"


class Node:
    """Node class that we've used in lectures."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    rest_max = max(head.next)
    return head.value if head.value > rest_max else rest_max


def linkify(items: list[int], index: int = 0) -> Node | None:
    if index >= len(items):
        return None
    else:
        current_node = Node(items[index], linkify(items, index + 1))
        return current_node


def scale(head: Node | None, factor: int) -> Node | None:
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
