def plunder(towns, town, people_killed, gold_plundered):
    towns[town]["population"] -= people_killed
    towns[town]["gold"] -= gold_plundered
    print(f"{town} plundered! {gold_plundered} gold stolen, {people_killed} citizens killed.")

    if towns[town]["population"] <= 0 or towns[town]["gold"] <= 0:
        print(f"{town} has been wiped off the map!")
        del towns[town]

    return towns


def prosper(towns, town, gold):
    if gold > 0:
        towns[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")

    return towns


def main():

    # Building the towns dict off of input commands
    towns = {}
    while True:
        command = input().split("||")

        if command[0] == "Sail":
            break

        city, population, gold = command
        population, gold = int(population), int(gold)

        if city not in towns.keys():
            towns[city] = {"population": population, "gold": gold}
        else:
            towns[city]["population"] += population
            towns[city]["gold"] += gold

    # Looping over commands for towns dict manipulation
    while True:
        command = input().split("=>")

        # Breaking when receiving "End"
        if command[0] == "End":
            break

        # Handling possible cases with functions
        if command[0] == "Plunder":
            town, people_killed, gold_plundered = command[1], int(command[2]), int(command[3])
            towns = plunder(towns, town, people_killed, gold_plundered)

        elif command[0] == "Prosper":
            town, gold = command[1], int(command[2])
            towns = prosper(towns, town, gold)

    # Final printouts
    if len(towns.keys()) > 0:
        print(f"Ahoy, Captain! There are {len(towns.keys())} wealthy settlements to go to:")
        for town, details in towns.items():
            print(f"{town} -> Population: {details['population']} citizens, Gold: {details['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


if __name__ == "__main__":
    main()
