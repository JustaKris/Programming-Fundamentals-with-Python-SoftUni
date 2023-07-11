travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for command in travel_route:
    if command != "Titan":
        command = command.split()

        if command[0] == "Travel":
            light_years = int(command[1])

            if fuel >= light_years:
                fuel -= light_years
                print(f"The spaceship travelled {light_years} light-years.")

            else:
                print("Mission failed.")
                break

        elif command[0] == "Enemy":
            enemy_armour = int(command[1])

            if ammunition >= enemy_armour:
                ammunition -= enemy_armour
                print(f"An enemy with {enemy_armour} armour is defeated.")

            elif fuel >= enemy_armour * 2:
                fuel -= enemy_armour * 2
                print(f"An enemy with {enemy_armour} armour is outmaneuvered.")

            else:
                print("Mission failed.")
                break

        elif command[0] == "Repair":
            supplies = int(command[1])
            fuel += supplies
            ammunition += supplies * 2
            print(f"Ammunitions added: {supplies * 2}.")
            print(f"Fuel added: {supplies}.")

    else:
        print("You have reached Titan, all passengers are safe.")


'''
Travel 20||Enemy 50||Enemy 50||Enemy 10||Repair 15||Enemy 50||Titan
60
100
'''