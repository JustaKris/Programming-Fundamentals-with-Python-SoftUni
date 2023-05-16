budget = int(input("What is our budget:"))
price = input("How much it costs:")
total_costs = 0
while price != "End":
    total_costs += int(price)
    if total_costs > budget:
        print("You went overdraft!")
        break
    price = input("How much it costs:")
else:
    print("You bought everything needed.")
