# Rock, Paper, Scissors v1
# Use string comparisons

import random

options: list[str] = ["Rock", "Paper", "Scissors"]

# Banner
print("Welcome to Rock, Paper, Scissors!")

# User chooses one option
user_hand: str = input("Choose your hand: ")

# CPU chooses randomly one option
cpu_hand: str = random.choice(options)
print(f"The cpu chose {cpu_hand}.")

# Calculate who wins
if (user_hand == "Rock"):
    if   (cpu_hand == "Rock"):
        print("Draw!")
    elif (cpu_hand == "Paper"):
        print("You lose!")
    elif (cpu_hand == "Scissors"):
        print("You win!")


elif (user_hand == "Paper"):
    if   (cpu_hand == "Rock"):
        print("You win!")
    elif (cpu_hand == "Paper"):
        print("Draw!")
    elif (cpu_hand == "Scissors"):
        print("You lose!")


elif (user_hand == "Scissors"):
    if   (cpu_hand == "Rock"):
        print("You lose!")
    elif (cpu_hand == "Paper"):
        print("You win!")
    elif (cpu_hand == "Scissors"):
        print("Draw!")
