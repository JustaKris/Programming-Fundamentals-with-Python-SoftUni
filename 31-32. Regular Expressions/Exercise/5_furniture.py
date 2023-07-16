import re

furniture_list = []
total_cost = 0
regex = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while True:
    line = input()

    if line == "Purchase":
        break

    match = re.search(regex, line)
    if match:
        furniture, price, quantity = match.groups()

        furniture_list.append(furniture)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
# print(*furniture_list, sep="\n")
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
