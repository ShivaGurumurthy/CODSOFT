import random
def get_user_choice():
    user_choice = input("Enter your choice: (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Enter your input from the following only: (rock, paper, scissors): ").lower()
    return user_choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "IT IS A TIE!!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "YOU WIN!!"
    else:
        return "YOU LOSE!!"
def play():
    print("Welcome to this Rock-Paper-Scissors Python Game......!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Your choice is: ", user_choice)
    print("Computer choice is: ", computer_choice)
    result = determine_winner(user_choice, computer_choice)
    print("The one who won this game is...: ", result)
play()