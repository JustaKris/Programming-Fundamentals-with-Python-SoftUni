pirate_ship = [int(section) for section in input().split(">")]
warship = [int(section) for section in input().split(">")]
max_hp_per_section = int(input())
command = input().split()

starting_pirate_ship = pirate_ship
# starting_warship = warship

game_ended = False
while command[0] != "Retire":

    if command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])

        if index in range(len(warship)):
            warship[index] -= damage

            if warship[index] <= 0:
                warship[index] = 0
                print("You won! The enemy ship has sunken.")
                game_ended = True
                break

    elif command[0] == "Defend":
        star_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])

        if star_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            for i in range(star_index, end_index + 1):
                pirate_ship[i] -= damage

                if pirate_ship[i] <= 0:
                    pirate_ship[i] = 0
                    print("You lost! The pirate ship has sunken.")
                    game_ended = True
                    break

    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])

        if index in range(len(pirate_ship)):
            pirate_ship[index] += health

            if pirate_ship[index] > max_hp_per_section:
                pirate_ship[index] = max_hp_per_section

    elif command[0] == "Status":
        repair_count = 0

        for i in range(len(pirate_ship)):
            if pirate_ship[i] < max_hp_per_section * 0.2:
                repair_count += 1

        if repair_count:
            print(f"{repair_count} sections need repair.")
            repair_count = 0

    if game_ended:
        break
    command = input().split()

else:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
