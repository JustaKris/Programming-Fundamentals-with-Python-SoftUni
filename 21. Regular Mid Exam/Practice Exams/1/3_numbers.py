numbers = [int(num) for num in input().split()]

average = sum(numbers) / len(numbers)

greater_numbers = sorted([num for num in numbers if num > average], reverse=True)

if greater_numbers:
    greater_numbers = [num for num in greater_numbers[:5]]
    print(*greater_numbers)
else:
    print("No")
