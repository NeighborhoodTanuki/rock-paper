import random

user_win = 0
computer_win = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    print("Computer choosed", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("Rock beat scissors, you won!")
        user_win += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("Paper beat rock, you won!")
        user_win += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("Scissors beat paper, you won!")
        user_win += 1

    elif user_input == computer_choice:
        print("Its a draw!")
        draws += 1

    else:
        print("You lost!")
        computer_win += 1

print("You won", user_win, "times.")
print("The computer won", computer_win, "times.")
print("You drew", draws, "times.")
print("See you!")

