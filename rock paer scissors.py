import random #importing module

#take user input
user_action = input("Enter a choice (rock, paper, scissors): ") #take input
possible_actions = ["rock", "paper", "scissors"]

#using choice function
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
#display both outputs which were selected by user and computer

#check condition to win who won the game
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("scissors cuts paper! you win!")
    else:
        print("rocks smashes scissors! you lose.")
        #take input for playing again 
        play_again = input("play again?   (y/n):")
        if play_again != "y":
        break