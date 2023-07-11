def add_card(deck, command):
    card = command[1]

    if card not in deck:
        deck.append(card)
        print("Card successfully added")
    else:
        print("Card is already in the deck")

    return deck


def remove_card(deck, command):
    card = command[1]

    if card in deck:
        deck.remove(card)
        print("Card successfully removed")
    else:
        print("Card not found")

    return deck


def remove_card_at(deck, command):
    index = int(command[1])

    if index in range(len(deck)):
        deck.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")

    return deck


def insert(deck, command):
    index, card = int(command[1]), command[2]

    if index in range(len(deck)):
        if card not in deck:
            deck.insert(index, card)
            print("Card successfully added")
        else:
            print("Card is already added")
    else:
        print("Index out of range")

    return deck


deck = input().split(", ")
number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split(", ")

    if command[0] == "Add":
        deck = add_card(deck, command)
    elif command[0] == "Remove":
        deck = remove_card(deck, command)
    elif command[0] == "Remove At":
        deck = remove_card_at(deck, command)
    elif command[0] == "Insert":
        deck = insert(deck, command)

print(*deck, sep=", ")
