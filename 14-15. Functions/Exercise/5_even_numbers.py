def even_only(numbers_list):
    return [number for number in numbers_list if number % 2 == 0]


# Lambda approach
# even_only_2 = lambda numbers_list: [number for number in numbers_list if number % 2 == 0]


numbers = list(map(int, input().split()))

print(even_only(numbers))
