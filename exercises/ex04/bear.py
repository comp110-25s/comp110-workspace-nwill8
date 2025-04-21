"""File to define Bear class."""

__author__ = "730580318"


class Bear:
    """New Bear class."""

    def __init__(self):
        """Initializing bear count of age and hunger score."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """The age and hunger score of the bear change each day!"""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """The hunger score increases as bears eat fish."""
        self.hunger_score += num_fish
