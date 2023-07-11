string = input()

letter_counter = {}
for element in string:
    if element != " ":
        if element not in letter_counter.keys():
            letter_counter[element] = 1
        else:
            letter_counter[element] += 1

for k, v in letter_counter.items():
    print(f"{k} -> {v}")
