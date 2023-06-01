def expense_calculator(item, quantity):
    coffee_price = 1.50
    water_price = 1.00
    coke_price = 1.40
    snacks_price = 2.00

    expenses = 0

    if item == 'coffee':
        expenses = coffee_price * quantity
    elif item == 'water':
        expenses = water_price * quantity
    elif item == 'coke':
        expenses = coke_price * quantity
    elif item == 'snacks':
        expenses = snacks_price * quantity

    print(f"{expenses:.2f}")


input_item = input()
input_quantity = int(input())

expense_calculator(input_item, input_quantity)
