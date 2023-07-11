companies = {}

while True:
    line = input()
    if line == "End":
        break

    company, id = line.split(" -> ")

    if company not in companies.keys():
        companies[company] = [id]
    else:
        if id not in companies[company]:
            companies[company].append(id)

for company, ids in companies.items():
    print(f"{company}")
    for id in ids:
        print(f"-- {id}")
