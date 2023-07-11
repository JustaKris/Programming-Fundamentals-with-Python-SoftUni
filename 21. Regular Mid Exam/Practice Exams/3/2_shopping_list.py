def urgent(groceries, command):

    item = command[1]
    if item not in groceries:
        groceries.insert(0, item)

    return groceries


def unnecessary(groceries, command):

    item = command[1]
    if item in groceries:
        groceries.remove(item)

    return groceries


def correct(groceries, command):

    old_item, new_item = command[1], command[2]
    if old_item in groceries:
        for i in range(len(groceries)):
            if groceries[i] == old_item:
                groceries[i] = new_item

    return groceries


def rearrange(groceries, command):

    item = command[1]
    if item in groceries:
        groceries.remove(item)
        groceries.append(item)

    return groceries


# Inputs
groceries = input().split("!")
command = input()

# Main loop
while command != "Go Shopping!":

    command = command.split()

    if "Urgent" in command:
        groceries = urgent(groceries, command)
    elif "Unnecessary" in command:
        groceries = unnecessary(groceries, command)
    elif "Correct" in command:
        groceries = correct(groceries, command)
    elif "Rearrange" in command:
        groceries = rearrange(groceries, command)

    command = input()

else:
    print(*groceries, sep=", ")
