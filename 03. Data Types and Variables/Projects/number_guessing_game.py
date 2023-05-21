"""
Guessing game
Try to guess the number
"""

import random

number = random.randint(1, 100)
# print(number)

guess_attempts = [0]
# print(guess_attempts)

print("--------------------------------------------")
print("This is a guessing game.")
print("I am thinking of a number from 1 to 100.\nHow quickly can you guess it?.")

# def guessing_game(): ???

while True:

    print("--------------------------------------------")
    guess = input("Enter your guess: ")

    # Option to exit the app
    if str(guess) == "exit":
        print("See you next time")
        break

    # checking if we have a valid input
    while True:
        try:
            guess = int(guess)
        except:
            print("--------------------------------------------")
            print("I said a NUMBER.... from 1 to 100!")
            print('Try again')
            print("--------------------------------------------")
            guess = input("Enter your guess: ")
            continue
        else:
            break

    guess_attempts.append(guess)
    # print(guess_attempts)

    # if guess = guess_attempts[-1]:

    # Can't compare strings to ints
    guess = int(guess)

    # Win scenarios
    if number == guess and len(guess_attempts) < 2:
        print("You cheated!!!")
        print("Congratulations....")
        print(f"Number of guesses: {len(guess_attempts)}")
        break
    elif number == guess and len(guess_attempts) <= 5:
        print("Congratulations!")
        print(f"Number of guesses: {len(guess_attempts)}")
        print("That was quick. Good job!")
        break
    elif number == guess and len(guess_attempts) <= 10:
        print("Congratulations!")
        print(f"Number of guesses: {len(guess_attempts)}")
        print("Decently fast!")
        break
    elif number == guess and len(guess_attempts) <= 15:
        print("Congratulations!")
        print(f"Number of guesses: {len(guess_attempts)}")
        print("I've seen quicker!")
        break
    elif number == guess and len(guess_attempts) <= 20:
        print("Congratulations!")
        print(f"Number of guesses: {len(guess_attempts)}")
        print("You sure took your sweet time...")
        break
    elif number == guess and len(guess_attempts) > 20:
        print("Well you took your sweet time...")
        print("Congratulations!")
        print(f"Number of guesses: {len(guess_attempts)}")

    # Guide
    if int(guess_attempts[-2]):

        if abs(number - guess) < abs(number - int(guess_attempts[-2])):
            print('Warmer')

        else:
            print('Colder')
    else:
        
        if guess < 1 or guess > 100:
            print("I said from 1 to 100...")
        
        if abs(number - guess) <= 3:
            print("My eyebrows are BURNING!!!")
        elif abs(number - guess) <= 5:
            print("Very warm")
        elif abs(number - guess) <= 10:
            print("Warm")
        elif abs(number - guess) <= 20:
            print("Tepid")
        else:
            print("Cold")
    """
    # Other guide
    if guess < 1 or guess > 100:
        print("I said from 1 to 100...")

    if abs(number - guess) <= 3:
        print("My eyebrows are BURNING!!!")
    elif abs(number - guess) <= 5:
        print("Very warm")
    elif abs(number - guess) <= 10:
        print("Warm")
    elif abs(number - guess) <= 20:
        print("Tepid")
    else:
        print("Cold")
    """