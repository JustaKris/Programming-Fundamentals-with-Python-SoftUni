budget = int(input())
price = input()

total_costs = 0
while price != "End":
    total_costs += int(price)
    if total_costs > budget:
        print("You went in overdraft!")
        break
    price = input()
else:
    print("You bought everything needed.")
