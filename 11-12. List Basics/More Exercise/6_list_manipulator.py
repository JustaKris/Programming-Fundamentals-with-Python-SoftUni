def manipulate_list(initial_list, commands):
    numbers = list(map(int, initial_list.split()))

    for command in commands:
        if command.startswith("exchange"):
            index = int(command.split()[1])
            if index < 0 or index >= len(numbers):
                print("Invalid index")
                continue
            numbers = numbers[index + 1:] + numbers[:index + 1]
        elif command.startswith("max"):
            _, parity = command.split()
            max_index = -1
            max_number = float("-inf")
            for i in range(len(numbers)):
                if numbers[i] % 2 == (0 if parity == "even" else 1):
                    if numbers[i] >= max_number:
                        max_number = numbers[i]
                        max_index = i
            if max_index == -1:
                print("No matches")
            else:
                print(max_index)
        elif command.startswith("min"):
            _, parity = command.split()
            min_index = -1
            min_number = float("inf")
            for i in range(len(numbers)):
                if numbers[i] % 2 == (0 if parity == "even" else 1):
                    if numbers[i] <= min_number:
                        min_number = numbers[i]
                        min_index = i
            if min_index == -1:
                print("No matches")
            else:
                print(min_index)
        elif command.startswith("first"):
            _, count, parity = command.split()
            count = int(count)
            if count > len(numbers):
                print("Invalid count")
                continue
            result = []
            for num in numbers:
                if num % 2 == (0 if parity == "even" else 1):
                    result.append(num)
                    if len(result) == count:
                        break
            print(result)
        elif command.startswith("last"):
            _, count, parity = command.split()
            count = int(count)
            if count > len(numbers):
                print("Invalid count")
                continue
            result = []
            for num in reversed(numbers):
                if num % 2 == (0 if parity == "even" else 1):
                    result.insert(0, num)
                    if len(result) == count:
                        break
            print(result)
        elif command == "end":
            break

    print(numbers)


initial_list = input()
commands = []
while True:
    command = input()
    if command == "end":
        break
    commands.append(command)

manipulate_list(initial_list, commands)