numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

greater_numbers = [num for num in numbers if num > average].sort(reverse=True)

greater_numbers = [str(num) for num in greater_numbers[:5]]
result = " ".join(greater_numbers)
print(result)
