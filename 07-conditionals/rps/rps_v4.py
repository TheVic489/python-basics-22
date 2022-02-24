"""
Rock, Paper, Scissors v4.

- Wrap your code in functions.
- Use pure functions except the input and output functions.
"""

import random

# ---------------------------------------------------------------------
def print_banner() -> None:
    """Prints the welcome banner."""

    print("Welcome to the 'Rock, Paper, Scissors' game!")


# ---------------------------------------------------------------------
def get_hands() -> tuple[str, str]:
    """Returns player and cpu hands"""

    # User chooses one option
    user_hand: str = input("Choose your hand: ")

    # CPU chooses randomly one option
    options:  list[str] = ["Rock", "Paper", "Scissors"]
    cpu_hand: str       = random.choice(options)
    print(f"The cpu chose {cpu_hand}.")

    return user_hand, cpu_hand


# Pure function!
# ---------------------------------------------------------------------
def match(user_hand: str, cpu_hand: str) -> int:
    """Returns an int corresponding to the result of the match.
       -1 = The user lost.
        0  = Draw game.
        1  = The user won.
    """

    # Declare variables
    user_rock:     bool = (user_hand == "Rock")
    user_paper:    bool = (user_hand == "Paper")
    user_scissors: bool = (user_hand == "Scissors")

    cpu_rock:      bool = (cpu_hand == "Rock")
    cpu_paper:     bool = (cpu_hand == "Paper")
    cpu_scissors:  bool = (cpu_hand == "Scissors")

    result: int

    # User chooses Rock
    if user_rock and cpu_rock:
        result = 0
    elif user_rock and cpu_paper:
        result = -1
    elif user_rock and cpu_scissors:
        result = 1
    # User chooses Paper
    elif user_paper and cpu_rock:
        result = 1
    elif user_paper and cpu_paper:
        result = 0
    elif user_paper and cpu_scissors:
        result = -1
    # User chooses Scissors
    elif user_scissors and cpu_rock:
        result = -1
    elif user_scissors and cpu_paper:
        result = 1
    elif user_scissors and cpu_scissors:
        result = 0

    return result


# ---------------------------------------------------------------------
def print_result(result: int) -> None:
    """Prints the result as a string."""

    if   (result < 0):
        print("You lose.")
    elif (result == 0):
        print("Draw game.")
    elif (result > 0):
        print("You win.")


# Main
# ---------------------------------------------------------------------
def main() -> None:
    """Runs the Rock, Paper, Scissors game."""

    print_banner()

    user_hand, cpu_hand = get_hands()
    match_result: int   = match(user_hand, cpu_hand)

    print_result(match_result)


# ---------------------------------------------------------------------
main()
# ---------------------------------------------------------------------
