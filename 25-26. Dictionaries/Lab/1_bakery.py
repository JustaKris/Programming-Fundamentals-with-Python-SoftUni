food = [item for item in input().split()]

stock = {}
for i in range(0, len(food), 2):
    product = food[i]
    quantity = int(food[i + 1])
    stock[product] = quantity

print(stock)
