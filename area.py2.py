import random

def format_output(message):
    """Formats the output message with stars."""
    return f"***** {message} *****"

def get_user_choice():
    """Prompts the user to enter their choice and checks for invalid inputs."""
    while True:
        try:
            choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if choice not in [1, 2, 3]:
                print(format_output("Please enter a  valid number between 1 and 3."))
            else:
                return choice
        except ValueError:
            print(format_output("Please enter a number between 1 and 3."))

def who_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win"
    else:
        return "You lose"