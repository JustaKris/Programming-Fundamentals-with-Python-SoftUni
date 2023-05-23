budget = float(input())
price_flower = float(input())

price_egg = price_flower * 0.75
price_milk = price_flower * 1.25
price_per_easter_bread = price_flower + price_egg + (price_milk * 0.25)

total_costs = 0
number_of_loaves = 0
colored_eggs = 0
while budget > total_costs:
    previous_total_costs = total_costs
    total_costs += price_per_easter_bread
    # total_costs += price_flower + price_egg
    # if number_of_loaves == 0 or number_of_loaves % 4 == 0:
    #     total_costs += price_milk
    if total_costs > budget:
        total_costs = previous_total_costs
        break
    colored_eggs += 3
    number_of_loaves += 1
    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2
money_left = budget - total_costs
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")