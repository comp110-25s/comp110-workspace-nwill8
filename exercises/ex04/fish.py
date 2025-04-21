"""File to define Fish class."""

__author__ = "730580318"


class Fish:
    """New fish class."""

    def __init__(self):
        """Initializing fish count of age."""
        self.age = 0

    def one_day(self):
        """Fish's age increases each day."""
        self.age += 1
