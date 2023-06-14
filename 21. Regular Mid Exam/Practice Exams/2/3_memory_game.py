sequence = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        break

    index1, index2 = map(int, command.split())

    if index1 == index2 or index1 < 0 or index1 >= len(sequence) or index2 < 0 or index2 >= len(sequence):
        middle_index = len(sequence) // 2
        moves += 1
        element = f"-{moves}a"
        sequence.insert(middle_index, element)
        sequence.insert(middle_index, element)
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence[index1] == sequence[index2]:
        element = sequence[index1]
        del sequence[max(index1, index2)]
        del sequence[min(index1, index2)]
        moves += 1
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print("Try again!")

if not sequence:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")
