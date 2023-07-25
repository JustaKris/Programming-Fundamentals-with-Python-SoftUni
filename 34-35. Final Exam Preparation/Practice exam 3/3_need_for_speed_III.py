def drive(cars, car, distance, fuel_required):
    if cars[car]["fuel"] > fuel_required:
        cars[car]["fuel"] -= fuel_required
        cars[car]["mileage"] += distance
        print(f"{car} driven for {distance} kilometers. {fuel_required} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")

    if cars[car]["mileage"] >= 100000:
        print(f"Time to sell the {car}!")
        del cars[car]

    return cars


def refuel(cars, car, fuel):
    current_fuel = cars[car]["fuel"]
    cars[car]["fuel"] += fuel
    if cars[car]["fuel"] > 75:
        fuel = 75 - current_fuel
        cars[car]["fuel"] = 75
    print(f"{car} refueled with {fuel} liters")

    return cars


def revert(cars, car, kilometers):
    if cars[car]["mileage"] - kilometers >= 10000:
        cars[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        cars[car]["mileage"] = 10000

    return cars


def main():
    # Reading number of cars to expect
    number_of_cars = int(input())

    # Building the cars dict
    cars = {}
    for _ in range(number_of_cars):
        car, mileage, fuel = input().split("|")
        mileage, fuel = int(mileage), int(fuel)
        cars[car] = {
            "mileage": mileage,
            "fuel": fuel
        }

    # Logic loop for command inputs
    while True:
        command, *details = input().split(" : ")

        if command == "Stop":
            break

        # Command checks
        if command == "Drive":
            car, distance, fuel_required = details
            distance, fuel_required = int(distance), int(fuel_required)
            cars = drive(cars, car, distance, fuel_required)

        if command == "Refuel":
            car, fuel = details
            fuel = int(fuel)
            cars = refuel(cars, car, fuel)

        if command == "Revert":
            car, kilometers = details
            kilometers = int(kilometers)
            cars = revert(cars, car, kilometers)

    # Final printouts
    for car, info in cars.items():
        print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")


if __name__ == "__main__":
    main()
