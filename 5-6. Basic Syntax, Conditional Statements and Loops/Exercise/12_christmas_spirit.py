number_of_decorations = int(input())
days_until_xmas = int(input())

# Saving costs and spirit per item in lists
ornament_set = [2, 5]
tree_skirt = [5, 3]
tree_garland = [3, 10]
tree_lights = [15, 17]

total_costs = 0
total_spirit = 0

for day in range(1, days_until_xmas + 1):
    if day % 11 == 0:
        number_of_decorations += 2
    if day % 2 == 0:
        total_costs += ornament_set[0] * number_of_decorations
        total_spirit += ornament_set[1]
    if day % 3 == 0:
        total_costs += (tree_skirt[0] + tree_garland[0]) * number_of_decorations
        total_spirit += tree_skirt[1] + tree_garland[1]
    if day % 5 == 0:
        total_costs += tree_lights[0] * number_of_decorations
        total_spirit += tree_lights[1]
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_costs += tree_skirt[0] + tree_garland[0] + tree_lights[0]

if days_until_xmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {total_spirit}")