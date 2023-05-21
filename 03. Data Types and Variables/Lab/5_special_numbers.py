number = int(input())

special_number = [5, 7, 11]
for num in range(1, number + 1):
    list_nums = [i for i in str(num)]

    total = 0
    for j in list_nums:
        total += int(j)
    if total in special_number:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
