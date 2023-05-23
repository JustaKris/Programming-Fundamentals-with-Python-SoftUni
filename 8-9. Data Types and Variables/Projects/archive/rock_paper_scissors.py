"""
Rock, Paper, Scissors
"""

# Ask the players if they want to play
while True:
    print('------------------------------------------------------------')
    ready = input("Rock, paper, scissors? Y/N:")

    if ready[0].lower() == "y":

        rules = ["rock", "paper", "scissors"]

        # def player_1():

        # Player one input and validity check
        print('------------------------------------------------------------')
        player_1_input = str(input("Player 1: rock, paper or scissors?\n|-->").lower())

        while True:

            if player_1_input not in rules:
                print('------------------------------------------------------------')
                print("Nope!")
                print("Rock, paper or scissors...")
                player_1_input = str(input("Player 1: rock, paper or scissors?\n|-->"))

            else:
                break

        # Player two input and validity check
        print('------------------------------------------------------------')
        player_2_input = str(input("Player 2: rock, paper or scissors?\n|-->").lower())

        while True:

            if player_2_input not in rules:
                print('------------------------------------------------------------')
                print("Nope!")
                print("Rock, paper or scissors...")
                player_2_input = str(input("Player 2: rock, paper or scissors?\n|-->"))

            else:
                break

        print('------------------------------------------------------------')
        # Win conditions
        player_1 = player_1_input
        player_2 = player_2_input

        if player_1 == 'rock' and player_2 == 'scissors':
            print('|------------------|')
            print('|> Player 1 WINS! <|')
            print('|------------------|')

        elif player_1 == 'paper' and player_2 == 'rock':
            print('|------------------|')
            print('|> Player 1 WINS! <|')
            print('|------------------|')

        elif player_1 == 'scissors' and player_2 == 'paper':
            print('|------------------|')
            print('|> Player 1 WINS! <|')
            print('|------------------|')


        elif player_2 == 'rock' and player_1 == 'scissors':
            print('|------------------|')
            print('|> Player 2 WINS! <|')
            print('|------------------|')

        elif player_2 == 'paper' and player_1 == 'rock':
            print('|------------------|')
            print('|> Player 2 WINS! <|')
            print('|------------------|')

        elif player_2 == 'scissors' and player_1 == 'paper':
            print('|------------------|')
            print('|> Player 2 WINS! <|')
            print('|------------------|')

        else:
            print("Draw!!!")

    else:
        print("|----------------------|")
        print("|> Back to work then! <|")
        print("|----------------------|")
        break
