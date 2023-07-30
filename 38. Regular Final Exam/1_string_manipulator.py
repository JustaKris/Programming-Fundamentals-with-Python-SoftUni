string = input()

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'Translate':
        char, replacement = command[1:]
        string = string.replace(char, replacement)
        print(string)
    elif command[0] == 'Includes':
        substring = command[1]
        print(substring in string)
    elif command[0] == 'Start':
        substring = command[1]
        print(string.startswith(substring))
    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif command[0] == 'FindIndex':
        char = command[1]
        # print(f"Test - {string}")
        # for i in range(0, len(string), -1):
        for i in reversed(range(len(string))):
            # print(f"Test - {i}")
            if string[i] == char:
                print(i)
                break
    elif command[0] == 'Remove':
        start_index, count = int(command[1]), int(command[2])
        string = string[:start_index] + string[start_index + count:]
        print(string)

'''
//Thi5 I5 MY 5trING!//
Translate 5 s
Includes string
Start //This
Lowercase
FindIndex i
Remove 0 10
End
'''