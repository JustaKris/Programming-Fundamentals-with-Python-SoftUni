n_orders = int(input())

total_cost = 0
for order in range(n_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.01 or days not in range(1, 32) or capsules_per_day not in range(1, 2001):
        continue

    spent_today = price_per_capsule * capsules_per_day * days
    total_cost += spent_today

    print(f"The price for the coffee is: ${spent_today:.2f}")
print(f"Total: ${total_cost:.2f}")

