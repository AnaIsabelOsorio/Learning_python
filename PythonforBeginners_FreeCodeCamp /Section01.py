import random  # This module allows us to generate random choices for the computer

# Explain to the user what the game is about
print("Welcome to Rock, Paper, Scissors!")
print("You will play against the computer.")

# Create a list of choices
choices = ["rock", "paper", "scissors"]

# Ask the player for their choice
# input() function gets user input as a string
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
# .lower() converts the input to lowercase so it matches our list even if user typed "Rock" or "ROCK"

# Check if the player choice is valid
if player_choice not in choices:
    print("Invalid choice. Please restart and choose rock, paper, or scissors.")
else:
    # Computer makes a random choice from the list using random.choice()
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    # Compare the choices to determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
