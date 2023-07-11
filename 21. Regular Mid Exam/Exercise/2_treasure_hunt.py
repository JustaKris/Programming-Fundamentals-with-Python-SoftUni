loot = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()
    # if command == "Yohoho!":
    #     break

    if command[0] == "Loot":
        items = command[1:]
        for item in items:
            if item not in loot:
                loot.insert(0, item)
    elif command[0] == "Drop":
        index = int(command[1])
        if index not in range(len(loot)):
            command = input()
            continue
        loot.append(loot.pop(index))
    elif command[0] == "Steal":
        count = int(command[1])
        stolen = loot[len(loot) - count:]
        loot = loot[:len(loot) - count]
        print(*stolen, sep=", ")

    command = input()


if not loot:
    print("Failed treasure hunt.")
else:
    total_gain = sum([len(item) for item in loot])
    average_gain = total_gain / len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
