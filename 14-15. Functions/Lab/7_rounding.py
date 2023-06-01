def rounder(numbers_list):
    return [round(float(x)) for x in numbers_list.split()]


numbers = input()

print(rounder(numbers))
