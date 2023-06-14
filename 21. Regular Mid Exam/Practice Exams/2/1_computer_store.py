total_cost = 0
total_tax = 0
total_price_without_tax = 0
while True:
    part_price = input()
    if part_price == "special":
        if total_cost <= 0:
            print("Invalid order!")
            break
        else:
            total_cost *= 0.9
            print(f"Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_without_tax:.2f}$")
            print(f"Taxes: {total_tax:.2f}$")
            print("-----------")
            print(f"Total price: {total_cost:.2f}$")
            break

    elif part_price == "regular":
        if total_cost <= 0:
            print("Invalid order!")
            break
        else:
            print(f"Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {total_price_without_tax:.2f}$")
            print(f"Taxes: {total_tax:.2f}$")
            print("-----------")
            print(f"Total price: {total_cost:.2f}$")
            break
    else:
        part_price = float(part_price)
        if part_price < 0:
            print("Invalid price!")
            continue
        total_cost += part_price * 1.2
        total_tax += part_price * 0.2
        total_price_without_tax += part_price
