import re


def validate_destination(destination_data):
    travel_points = 0
    valid_destinations = []

    pattern = r'(\=|\/)([A-Z][A-Za-z]{2,})\1'
    result = re.findall(pattern, destination_data)

    for el in result:
        valid_destinations.append(el[1])
        travel_points += len(el[1])

    return valid_destinations, travel_points


destination_data = input()

destinations, travel_points = validate_destination(destination_data)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
