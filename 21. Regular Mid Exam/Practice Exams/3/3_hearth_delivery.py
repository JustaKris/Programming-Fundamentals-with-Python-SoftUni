neighborhood = [int(house) for house in input().split("@")]
jump_command = input()

current_index = 0
while jump_command != "Love!":

    # Index setup and check
    index = int(jump_command.split()[1])
    current_index += index
    if current_index not in range(len(neighborhood)):
        current_index = 0

    if neighborhood[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
        jump_command = input()
        continue
    else:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] <= 0:
            neighborhood[current_index] = 0
            print(f"Place {current_index} has Valentine's day.")

    jump_command = input()

else:
    print(f"Cupid's last position was {current_index}.")

    if sum(neighborhood) <= 0:
        print("Mission was successful.")
    else:
        failed_households = [house for house in neighborhood if house > 0]
        print(f"Cupid has failed {len(failed_households)} places.")
