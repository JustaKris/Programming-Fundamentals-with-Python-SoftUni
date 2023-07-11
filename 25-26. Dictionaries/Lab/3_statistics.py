food = {}
while True:
    command = input()

    if command == "statistics":
        break

    product, quantity = command.split(": ")
    if product in food.keys():
        food[product] += int(quantity)
    else:
        food[product] = int(quantity)

print("Products in stock:")
for product, quantity in food.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(food.keys())}")
print(f"Total Quantity: {sum(food.values())}")

