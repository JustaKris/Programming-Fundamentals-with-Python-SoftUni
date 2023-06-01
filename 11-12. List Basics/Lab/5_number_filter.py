# Approach 1
# n = int(input())
#
# commands = ['even', 'odd', 'negative', 'positive']
# numbers = []
# filtered_numbers = []
#
# for i in range(n):
#     number = input()
#     numbers.append(int(number))
#
# command = input()
# if command == commands[0]:  # even
#     for number in numbers:
#         if number % 2 == 0:
#             filtered_numbers.append(number)
# elif command == commands[1]:  # odd
#     for number in numbers:
#         if number % 2 != 0:
#             filtered_numbers.append(number)
# if command == commands[2]:  # negative
#     for number in numbers:
#         if number < 0:
#             filtered_numbers.append(number)
# if command == commands[3]:  # positive
#     for number in numbers:
#         if number >= 0:
#             filtered_numbers.append(number)
#
# print(filtered_numbers)


# Approach 2
n = int(input())

even = 'even'
odd = 'odd'
negative = 'negative'
positive = 'positive'

numbers = [int(input()) for _ in range(n)]

filtered_numbers = []

command = input()

for num in numbers:
    filtered_command = (
        (command == even and num % 2 == 0) or
        (command == odd and num % 2 != 0) or
        (command == positive and num >= 0) or
        (command == even and num < 0)
    )

    if filtered_command:
        filtered_numbers.append(num)

print(filtered_numbers)