number_of_cities = int(input())

total_profit = 0.0

for i in range(1, number_of_cities + 1):

    city_name = input()
    earnings = float(input())
    expenses = float(input())

    if i % 5 == 0:
        earnings *= 0.9
    elif i % 3 == 0:
        expenses *= 1.5

    profit = earnings - expenses
    total_profit += profit

    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
