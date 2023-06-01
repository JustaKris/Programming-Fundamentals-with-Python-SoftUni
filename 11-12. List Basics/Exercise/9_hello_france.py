items = input().split("|")
budget = float(input())

starting_budget = budget
profits = []

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if item_type == "Clothes" and item_price > 50.00:
        continue
    elif item_type == "Shoes" and item_price > 35.00:
        continue
    elif item_type == "Accessories" and item_price > 20.50:
        continue

    if budget >= item_price:
        budget -= item_price
        profits.append(item_price * 1.4)

total = sum(profits) + budget
profit = total - starting_budget

for element in profits:
    print(f"{element:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")

if total >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
