numbers_list = list(map(int, input().split(", ")))

positive = [num for num in numbers_list if num >= 0]
print(f"Positive: {', '.join(map(str, positive))}")

negative = [num for num in numbers_list if num < 0]
print(f"Negative: {', '.join(map(str, negative))}")

even = [num for num in numbers_list if num % 2 == 0]
print(f"Even: {', '.join(map(str, even))}")

odd = [num for num in numbers_list if num % 2 != 0]
print(f"Odd: {', '.join(map(str, odd))}")
