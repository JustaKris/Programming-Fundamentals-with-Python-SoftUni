"""
Guessing game
Try to guess the number
"""

'''
secret_word = "word"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit:
    guess = input("Enter word: ")
    guess_count += 1
  else:
    out_of_guesses = True

if out_of_guesses:
  print("No more attempts left. You lost! Insert a coin to Continue")
else:
  print("You got it!")

'''

# Better guessing game

import random

# Instructions/intro
print("________________________________________________________________")
print("------------")
print("Instructions")
print("------------")
print("This is a guessing game.")
print("You need to guess the number i'm thiking of.")
print("Just enter your guess with the keyboard and press 'Enter'.")
print("The game should guide you to the right answer... hopefully.")
print("'Warmer' signifies that your current guess is closer than your previous one and the reverse for 'Colder'.")
print("Good luck!!!")
print("________________________________________________________________")
print("\n")
# Prep
guess_list = [0]
number = random.randint(1, 100)

# Logic
while True:

    # For testing purposes
    # print(number)

    player_guess = int(input("What number am i thinking of: "))

    if player_guess < 1 or player_guess > 100:
        print("---------------------------")
        print("Between 1 and 100...")
        print("---------------------------")
        continue

    if player_guess == number and len(guess_list) < 2:
        print("-----------")
        print("!!!HACKS!!!")
        print("-----------")
        break

    elif player_guess == number and len(guess_list) < 4:
        print("----------------------")
        print("Well that was quick...")
        print("----------------------")
        break

    elif player_guess == number:
        print("------------------------------------------------------------------")
        print(f"Congratulation, you guessed it in only {len(guess_list)} attempts!!")
        print("------------------------------------------------------------------")
        break

    elif player_guess == number and len(guess_list) < 25:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"At long last!!! Congratulations, you guessed it in only {len(guess_list)} attempts!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break

    guess_list.append(player_guess)

    if guess_list[-2]:
        if abs(number - player_guess) < abs(number - guess_list[-2]):
            print("Warmer")

        else:
            print("Colder")

    else:
        if abs(number - player_guess) <= 3:
            print("Almost psychic!!!")

        elif abs(number - player_guess) <= 7:
            print("I'm starting to sweat!")

        elif abs(number - player_guess) <= 10:
            print("Warm")

        else:
            print("Cold")
