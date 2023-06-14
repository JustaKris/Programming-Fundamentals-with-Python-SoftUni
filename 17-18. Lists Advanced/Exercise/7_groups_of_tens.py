numbers = list(map(int, input().split(", ")))

group = 10
while numbers:
    group_list = []
    for number in numbers:
        if number <= group:
            group_list.append(number)
    print(f"Group of {group}'s: {group_list}")
    group += 10
    numbers = [number for number in numbers if number not in group_list]
