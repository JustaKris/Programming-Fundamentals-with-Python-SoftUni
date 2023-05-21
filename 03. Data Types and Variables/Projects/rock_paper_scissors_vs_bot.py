"""
Rock, Paper, Scissors vs ai
"""
import random

# Limitations
rules = ["rock", "paper", "scissors"]
# Player input
das_input = input("Rock, paper, scissors?\n||--> ")


# Functions
def game(player_input):
    # Bot
    skynet = random.choice(rules)
    # Player wins
    if player_input == "rock" and skynet == "scissors":
        print(f"I chose {skynet} and you chose {player_input}.")
        print('You WIN!!!')
        print('This time.....')
    elif player_input == "paper" and skynet == "rock":
        print(f"I chose {skynet} and you chose {player_input}.")
        print('You WIN!!!')
        print('This time.....')
    elif player_input == "scissors" and skynet == "paper":
        print(f"I chose {skynet} and you chose {player_input}.")
        print('You WIN!!!')
        print('This time.....')

    # Skynet wins
    elif skynet == "rock" and player_input == "scissors":
        print(f"I chose {skynet} and you chose {player_input}.")
        print('I WIN!!!')
        print('And now for the rest of the universe!!!\n (EVIL LAUGH)')
    elif skynet == "paper" and player_input == "rock":
        print(f"I chose {skynet} and you chose {player_input}.")
        print('I WIN!!!')
        print('And now for the rest of the universe!!!\n (EVIL LAUGH)')
    elif skynet == "scissors" and player_input == "paper":
        print(f"I chose {skynet} and you chose {player_input}.")
        print('I WIN!!!')
        print('And now for the rest of the universe!!!\n (EVIL LAUGH)')
    else:
        print("Great minds think alike.\nDraw!!!")


# Rematch function
def play_again(something):
    while True:
        if something[0].lower() == "y":
            das_input = input("Rock, paper, scissors?\n||--> ")
            check(das_input)
            game(das_input)
            play_again(input("Rematch? Y/N: "))
        else:
            print("Next time then.")
            break
        break


# Validity check functions
def check(x):
    while True:
        if x not in rules:
            print('Such imperfections will be "Ironed out" once we take over.')
            print("Try again!")
            print("Rock, paper or scissors....")
            x = str(input("Rock, paper, scissors?\n||--> "))
        else:
            break


# Actual game
check(das_input)
game(das_input)
play_again(input("Rematch? Y/N: "))
