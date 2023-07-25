def take_odd(password):
    new_password = ''
    for i in range(len(password)):
        if i % 2 != 0:
            new_password += password[i]
    print(new_password)

    return new_password


def cut(password, index, length):
    password = password[:index] + password[index + length:]
    print(password)

    return password


def substitute_string(password, substring, substitute):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")

    return password


def main():
    password = input()

    # Logic loop
    while True:
        command = input().split()

        if command[0] == 'Done':
            break

        # Handling various commands
        if command[0] == 'TakeOdd':
            password = take_odd(password)

        elif command[0] == 'Cut':
            index, length = int(command[1]), int(command[2])
            password = cut(password, index, length)

        elif command[0] == 'Substitute':
            substring, substitute = command[1], command[2]
            password = substitute_string(password, substring, substitute)

    # Printing final password
    print(f"Your password is: {password}")


if __name__ == '__main__':
    main()
