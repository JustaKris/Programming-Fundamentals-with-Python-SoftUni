def add_piece(pieces, piece, composer, key):
    if piece not in pieces.keys():
        pieces[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")

    return pieces


def remove_piece(pieces, piece):
    if piece in pieces.keys():
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return pieces


def change_key(pieces, piece, new_key):
    if piece in pieces.keys():
        pieces[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return pieces


# Read number of pieces
number_of_pieces = int(input())

# Setting up starting dictionary of pieces and their respective composers and keys
pieces = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

# Logic loop for incoming commands
while True:
    command, *params = input().split("|")

    if command == "Stop":
        break

    elif command == "Add":
        piece, composer, key = params
        pieces = add_piece(pieces, piece, composer, key)

    elif command == "Remove":
        piece = params[0]
        pieces = remove_piece(pieces, piece)

    elif command == "ChangeKey":
        piece, new_key = params
        pieces = change_key(pieces, piece, new_key)


# Printing contents of pieces dictionary
for piece, details in pieces.items():
    print(f"{piece} -> Composer: {details['composer']}, Key: {details['key']}")
