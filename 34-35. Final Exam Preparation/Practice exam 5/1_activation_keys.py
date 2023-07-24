def contains(activation_key, substring):
    if substring in activation_key:
        return f"{activation_key} contains {substring}"
    else:
        return "Substring not found!"


def flip_string(activation_key, case, start_index, end_index):
    if case == "Upper":
        activation_key = activation_key[:start_index] + \
                         activation_key[start_index:end_index].upper() + activation_key[end_index:]
    else:
        activation_key = activation_key[:start_index] + \
                         activation_key[start_index:end_index].lower() + activation_key[end_index:]
    return activation_key


def slice_string(activation_key, start_index, end_index):
    activation_key = activation_key[:start_index] + activation_key[end_index:]
    return activation_key


def logic_loop(activation_key):
    while True:
        command = input().split(">>>")

        if command[0] == "Generate":
            break

        if command[0] == "Contains":
            substring = command[1]
            print(contains(activation_key, substring))

        elif command[0] == "Flip":
            case, start_index, end_index = command[1], int(command[2]), int(command[3])
            activation_key = flip_string(activation_key, case, start_index, end_index)
            print(activation_key)

        elif command[0] == "Slice":
            start_index, end_index = int(command[1]), int(command[2])
            activation_key = slice_string(activation_key, start_index, end_index)
            print(activation_key)

    return activation_key


def main():
    activation_key = input()
    activation_key = logic_loop(activation_key)
    print(f"Your activation key is: {activation_key}")


if __name__ == "__main__":
    main()
