def rate(plants, plant, rating):
    plants[plant]["ratings"].append(rating)
    return plants


def update(plants, plant, new_rarity):
    plants[plant]["rarity"] = new_rarity
    return plants


def reset(plants, plant):
    plants[plant]["ratings"] = []
    return plants


def main():
    # Reading number of plants
    number_of_plants = int(input())

    # Building the plants dictionary
    plants = {}
    for _ in range(number_of_plants):
        plant, rarity = input().split("<->")
        rarity = int(rarity)
        plants[plant] = {
            "rarity": rarity,
            "ratings": []
        }

    # Logic loop for command inputs
    while True:
        line = input().split(": ")

        # Exit loop when receiving command "Exhibition"
        if line[0] == "Exhibition":
            break

        if line[1].split(" - ")[0] in plants.keys():
            if line[0] == "Rate":
                plant, rating = line[1].split(" - ")
                rating = float(rating)
                plants = rate(plants, plant, rating)

            elif line[0] == "Update":
                plant, new_rarity = line[1].split(" - ")
                new_rarity = int(new_rarity)
                plants = update(plants, plant, new_rarity)

            elif line[0] == "Reset":
                plant = line[1]
                plants = reset(plants, plant)

        # If plant not present in the plants dictionary
        else:
            print("error")

    # Final printouts
    print("Plants for the exhibition:")
    for plant, info in plants.items():
        rarity = info["rarity"]
        average_rating = sum(info["ratings"]) / len(info["ratings"]) if info["ratings"] else 0.0
        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


if __name__ == '__main__':
    main()
