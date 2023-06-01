def min_max_sum(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    sum_value = sum(numbers_list)

    print(f"The minimum number is {min_value}")
    print(f"The maximum number is {max_value}")
    print(f"The sum number is: {sum_value}")


numbers = list(map(int, input().split()))
min_max_sum(numbers)
