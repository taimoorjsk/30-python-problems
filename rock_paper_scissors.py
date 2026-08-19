# Problem: Rock Paper Scissors
# Interactive game where the user plays rock, paper, or scissors against
# a random computer choice. Determines and displays the winner or a tie.

import random

def play_rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']

    user_input = input("Enter rock, paper, or scissors: ").strip().lower()

    if user_input not in choices:
        print("Invalid input. Please run the program again and enter rock, paper, or scissors.")
        return

    computer_selection = random.choice(choices)

    print(f"Input from user: {user_input}")
    print(f"Random selection from computer: {computer_selection}")

    if user_input == computer_selection:
        print("Output: It's a tie!")
    elif (user_input == 'rock' and computer_selection == 'scissors') or \
         (user_input == 'paper' and computer_selection == 'rock') or \
         (user_input == 'scissors' and computer_selection == 'paper'):
        print("Output: User won")
    else:
        print("Output: Computer won")

if __name__ == "__main__":
    play_rock_paper_scissors()
