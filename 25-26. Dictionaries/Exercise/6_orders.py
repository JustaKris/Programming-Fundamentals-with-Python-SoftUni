products = {}

while True:
    line = input()

    if line == "buy":
        break

    name, price, quantity = line.split(" ")
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

for name, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{name} -> {total_price:.2f}")

# Inputs
'''
Beer 2.20 100
IceTea 1.50 50
NukaCola Practice exam 1.30 80
Water 1.00 500
buy
'''