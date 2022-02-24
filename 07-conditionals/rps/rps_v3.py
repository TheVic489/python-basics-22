# Rock, Paper, Scissors v3
# Use boolean operators

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


# User chooses Rock
if user_rock and cpu_rock:
        print("Draw!")
elif user_rock and cpu_paper:
    print("You lose!")
elif user_rock and cpu_scissors:
    print("You win!")
# User chooses Paper
elif user_paper and cpu_rock:
    print("You win!")
elif user_paper and cpu_paper:
    print("Draw!")
elif user_paper and cpu_scissors:
    print("You lose!")
# User chooses Scissors
elif user_scissors and cpu_rock:
        print("You lose!")
elif user_scissors and cpu_paper:
        print("You win!")
elif user_scissors and cpu_scissors:
        print("Draw!")
