# Inputs
# divisor = int(input("Give me a divisor:"))
# boundary = int(input("Give me a boundary:"))
divisor = int(input())
boundary = int(input())

# Attempt 1
# largest_divisible = 0
# for number in range(divisor, boundary+1):
#     if number % divisor == 0:
#         result = number / divisor
#         if number > largest_divisible:
#             largest_divisible = number
# print(int(largest_divisible))

# Attempt 2
for number in range(boundary, divisor-1, -1):
    if number % divisor == 0:
        print(int(number))
        break
