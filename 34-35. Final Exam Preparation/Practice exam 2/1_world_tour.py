def add_stop(tour, index, location):
    if index in range(len(tour)):
        tour = tour[:index] + location + tour[index:]

    return tour


def remove_stop(tour, start_index, end_index):
    if start_index in range(len(tour)) and end_index in range(len(tour)):
        tour = tour[:start_index] + tour[end_index + 1:]

    return tour


def switch(tour, old_string, new_string):
    if old_string in tour:
        tour = tour.replace(old_string, new_string)

    return tour


def main():

    tour = input()

    while True:
        line = input().split(":")

        if line[0] == "Travel":
            break

        if line[0] == "Add Stop":
            index, location = int(line[1]), line[2]
            tour = add_stop(tour, index, location)

        elif line[0] == "Remove Stop":
            start_index, end_index = int(line[1]), int(line[2])
            tour = remove_stop(tour, start_index, end_index)

        elif line[0] == "Switch":
            old_string, new_string = line[1], line[2]
            tour = switch(tour, old_string, new_string)

        print(tour)

    print(f"Ready for world tour! Planned stops: {tour}")


if __name__ == '__main__':
    main()
