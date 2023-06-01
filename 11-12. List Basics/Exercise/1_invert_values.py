input_numbers_split = input().split()

reversed_numbers_split = []
for num in input_numbers_split:
    reversed_numbers_split.append(-int(num))

print(reversed_numbers_split)