resource_dict = {}

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    if resource not in resource_dict.keys():
        resource_dict[resource] = quantity
    else:
        resource_dict[resource] += quantity

for k, v in resource_dict.items():
    print(f"{k} -> {v}")
