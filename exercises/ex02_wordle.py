"""Creating my own Wordle program!"""

__author__: str = "730580318"


def contains_char(word: str, attempt: str) -> bool:
    """Is a single character found in the index of the first string"""

    assert len(attempt) == 1, f"len('{attempt}') is not 1)"

    index = 0
    while index < len(word):
        if word[index] == attempt:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Assigning emojis to letters in the guessed word"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    assert len(guess) == len(secret), "Guess must be the same length as secret"

    result = ""
    index = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """Requires the user to guess a word with a specific length"""
    guess = input(f"Enter a {expected_length} character word:")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program  and main game loop."""
    turns = 1
    max_turns = 6
    won = False

    while turns <= max_turns and not won:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
