def process_race_info(participants, info):
    racers = {participant: 0 for participant in participants}

    for data in info:
        name = "".join(filter(str.isalpha, data))
        distance = sum(int(digit) for digit in data if digit.isdigit())

        if name in racers:
            racers[name] += distance

    sorted_racers = sorted(racers.items(), key=lambda x: x[1], reverse=True)

    return sorted_racers[:3]


def main():
    participants = input().split(", ")
    race_info = []

    while True:
        data = input()
        if data == "end of race":
            break
        race_info.append(data)

    top_racers = process_race_info(participants, race_info)

    print("1st place:", top_racers[0][0])
    if len(top_racers) > 1:
        print("2nd place:", top_racers[1][0])
    if len(top_racers) > 2:
        print("3rd place:", top_racers[2][0])


if __name__ == "__main__":
    main()
