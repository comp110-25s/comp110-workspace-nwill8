"""Help to plan a cozy tea party!"""

__author__: str = "730580318"


def main_planner(guests: int) -> None:
    """A function to bring my functions together."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Number of tea bags needed based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats needed based on the number of teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of the tea bags and treats needed"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
