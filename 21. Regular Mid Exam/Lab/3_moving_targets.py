targets = [int(target) for target in input().split()]
command = input()

while command != "End":
    command = command.split()
    command[1], command[2] = int(command[1]), int(command[2])

    if int(command[1]) not in range(len(targets)) and command[0] == "Strike":
        print("Strike missed!")
        command = input()
        continue
    elif int(command[1]) not in range(len(targets)) and command[0] == "Add":
        print("Invalid placement!")
        command = input()
        continue
    elif int(command[1]) not in range(len(targets)):
        command = input()
        continue

    if "Shoot" in command[0]:
        index, power = int(command[1]), int(command[2])
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    elif "Add" in command[0]:
        index, value = int(command[1]), int(command[2])
        targets.insert(index, value)
    elif "Strike" in command[0]:
        index, radius = int(command[1]), int(command[2])

        if index not in range(len(targets)) \
            or index + 1 not in range(len(targets)) \
                or index - 1 not in range(len(targets)):
            print("Strike missed!")
        else:
            targets.pop(index + 1)
            targets.pop(index)
            targets.pop(index - 1)

    command = input()

else:
    print(*targets, sep="|")
