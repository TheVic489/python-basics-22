"""
Rock, Paper, Scissors v6.

- Check that inputs are correct.
- Allow to use only the initials r, p, s instead of Rock, Paper, Scissors
- Allow both lowercase and uppercase letters.
"""

import random
import sys


# ---------------------------------------------------------------------
# Input functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
def validate(user_input: str) -> str:
    """Returns one of the following three words:
       Rock, Paper, Scissors."""

    result: str
    cap_user_input: str = user_input.capitalize()

    if   "Rock".startswith(cap_user_input):
        result = "Rock"
    elif "Paper".startswith(cap_user_input):
        result = "Paper"
    elif "Scissors".startswith(cap_user_input):
        result = "Scissors"
    else:
        print("Error: Unknown hand!")
        sys.exit(2)
        
    return result


# ---------------------------------------------------------------------
def get_hands() -> tuple[str, str]:
    """Returns player and cpu hands"""

    # User chooses one option
    user_hand: str = validate(input("Choose your hand: "))

    # CPU chooses randomly one option
    hands:    list[str] = ["Rock", "Paper", "Scissors"]
    cpu_hand: str       = random.choice(hands)

    # Print hands
    print(f"You chose:     {user_hand}")
    print(f"The cpu chose: {cpu_hand}")

    return user_hand, cpu_hand


# ---------------------------------------------------------------------
# Print functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
def print_main_banner() -> None:
    """Prints the welcome banner."""

    print("Welcome to the 'Rock, Paper, Scissors' game!")


# ---------------------------------------------------------------------
def print_match_banner(match_id: int) -> None:
    """Prints the match banner."""

    print()
    print(f"Match No.{match_id} starts!")


# ---------------------------------------------------------------------
def print_match_result(user_points: int, cpu_points: int) -> None:
    """Prints the result as a string."""

    result:    tuple[int, int] = (user_points, cpu_points)

    you_lose:  tuple[int, int] = (0, 1)
    draw_game: tuple[int, int] = (0, 0)
    you_win:   tuple[int, int] = (1, 0)

    if   (result == you_lose):
        print("You lose.")
    elif (result == draw_game):
        print("Draw game.")
    elif (result == you_win):
        print("You win.")
    else:
        print("Error. Unexpected result!")


# ---------------------------------------------------------------------
def print_scores(user_score: int, cpu_score: int) -> None:
    """Prints the scores."""

    print(f"User: {user_score}, CPU: {cpu_score}")


# ---------------------------------------------------------------------
def print_end_game(user_score: int, cpu_score: int) -> None:
    """Prints the scores."""

    print()
    print("The game finished.")

    if user_score > cpu_score:
        print("Congratulations for winning!")


# ---------------------------------------------------------------------
# Match functions
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
def match(user_hand: str, cpu_hand: str) -> tuple[int, int]:
    """Returns a tuple corresponding to the result of the match.
       The first int is the user points and the second int is the cpu points.
       (1, 0) = The user won one point, the cpu won zero points.
       (0, 0) = Draw game.
       (0, 1) = The user won zero points, the cpu won one point.
    """

    # Declare variables
    user_rock:     bool = (user_hand == "Rock")
    user_paper:    bool = (user_hand == "Paper")
    user_scissors: bool = (user_hand == "Scissors")

    cpu_rock:      bool = (cpu_hand == "Rock")
    cpu_paper:     bool = (cpu_hand == "Paper")
    cpu_scissors:  bool = (cpu_hand == "Scissors")

    result: tuple[int, int]

    # User chooses Rock
    if user_rock and cpu_rock:
        result = (0, 0)
    elif user_rock and cpu_paper:
        result = (0, 1)
    elif user_rock and cpu_scissors:
        result = (1, 0)
    # User chooses Paper
    elif user_paper and cpu_rock:
        result = (1, 0)
    elif user_paper and cpu_paper:
        result = (0, 0)
    elif user_paper and cpu_scissors:
        result = (0, 1)
    # User chooses Scissors
    elif user_scissors and cpu_rock:
        result = (0, 1)
    elif user_scissors and cpu_paper:
        result = (1, 0)
    elif user_scissors and cpu_scissors:
        result = (0, 0)

    return result


# ---------------------------------------------------------------------
def play() -> tuple[int, int]:
    """Runs one match of the Rock, Paper, Scissors game.
       Returns the result of the match."""

    user_hand,   cpu_hand   = get_hands()
    user_points, cpu_points = match(user_hand, cpu_hand)
    print_match_result(user_points, cpu_points)

    return user_points, cpu_points


# Main
# ---------------------------------------------------------------------
def main() -> None:
    """Runs the Rock, Paper, Scissors game."""

    print_main_banner()

    user_score:  int = 0
    cpu_score:   int = 0

    num_matches: int = 3
    match_ids:   list[int] = list(range(1, num_matches+1))

    for match_id in match_ids:

        print_match_banner(match_id)

        user_points, cpu_points = play()

        user_score = user_score + user_points
        cpu_score  = cpu_score  + cpu_points

        print_scores(user_score, cpu_score)

    print_end_game(user_score, cpu_score)


# ---------------------------------------------------------------------
main()
# ---------------------------------------------------------------------
