"""File to define River class."""

__author__ = "730580318"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """New River class."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears!"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Animals must be removed when they pass away!"""
        surviving_fish = [fish for fish in self.fish if fish.age <= 3]
        surviving_bears = [bear for bear in self.bears if bear.age <= 5]
        self.fish = surviving_fish
        self.bears = surviving_bears

    def bears_eating(self) -> None:
        """Bears eat the fish to improve their hunger score!"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """If a bears hunger score gets to 0, they starve."""
        surviving_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = surviving_bears

    def repopulate_fish(self):
        """Fish produce offspring."""
        num_new_fish = (len(self.fish) // 2) * 4
        while num_new_fish > 0:
            self.fish.append(Fish())
            num_new_fish -= 1

    def repopulate_bears(self):
        """Bears produce offspring."""
        num_new_bears = len(self.bears) // 2
        while num_new_bears > 0:
            self.bears.append(Bear())
            num_new_bears -= 1

    def view_river(self):
        """To keep track of populations in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulating a week in the life of the river."""
        count = 0
        while count < 7:
            self.one_river_day()
            count += 1

    def remove_fish(self, amount: int) -> None:
        """Remove fish when they die."""
        self.fish = self.fish[amount:]
