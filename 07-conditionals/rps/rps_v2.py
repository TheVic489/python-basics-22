# Rock, Paper, Scissors v2
# Use boolean variables

import random

options: list[str] = ["Rock", "Paper", "Scissors"]

# Banner
print("Welcome to Rock, Paper, Scissors!")

# User chooses one option
user_hand: str = input("Choose your hand: ")

# CPU chooses randomly one option
cpu_hand: str = random.choice(options)
print(f"The cpu chose {cpu_hand}.")

# Declare variables
user_rock:     bool = (user_hand == "Rock")
user_paper:    bool = (user_hand == "Paper")
user_scissors: bool = (user_hand == "Scissors")

cpu_rock:      bool = (cpu_hand == "Rock")
cpu_paper:     bool = (cpu_hand == "Paper")
cpu_scissors:  bool = (cpu_hand == "Scissors")


# Calculate who wins
if user_rock:
    if   cpu_rock:
        print("Draw!")
    elif cpu_paper:
        print("You lose!")
    elif cpu_scissors:
        print("You win!")

elif user_paper:
    if   cpu_rock:
        print("You win!")
    elif cpu_paper:
        print("Draw!")
    elif cpu_scissors:
        print("You lose!")

elif user_scissors:
    if   cpu_rock:
        print("You lose!")
    elif cpu_paper:
        print("You win!")
    elif cpu_scissors:
        print("Draw!")
