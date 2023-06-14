numbers = list(map(int, input().split()))

command = input()
while command != "end":
    if "swap" in command:
        index1, index2 = map(int, command.split()[1:])
        # temp = numbers[index1]
        # numbers[index1] = numbers[index2]
        # numbers[index2] = temp
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif "multiply" in command:
        index1, index2 = map(int, command.split()[1:])
        numbers[index1] *= numbers[index2]
    elif "decrease" in command:
        numbers = [num-1 for num in numbers]
    command = input()

numbers = [str(x) for x in numbers]
result = ", ".join(numbers)

print(result)
