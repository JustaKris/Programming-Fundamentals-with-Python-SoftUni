def absoluter(list_of_numbers):
    return [abs(num) for num in list_of_numbers]


numbers = list(map(float, input().split()))
print(absoluter(numbers))
