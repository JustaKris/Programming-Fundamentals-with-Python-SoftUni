group_size = int(input())
number_of_days = int(input())

coins = 0
for day in range(1, number_of_days + 1):

    # Group size check
    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2

    coins += 50  # daily income
    coins -= 2 * group_size  # food expenditure

    if day % 3 == 0:
        coins -= 3 * group_size  # motivational party
    if day % 5 == 0:
        coins += 20 * group_size  # boss bonus
        if day % 3 == 0:
            coins -= 2 * group_size  # boss + motivational party tax

coins_per_companion = coins // group_size

print(f"{group_size} companions received {coins_per_companion} coins each.")