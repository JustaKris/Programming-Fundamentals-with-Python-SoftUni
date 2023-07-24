def insert_space(concealed_message, index):
    concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    print(concealed_message)

    return concealed_message


def reverse(concealed_message, substring):
    if substring in concealed_message:
        concealed_message = concealed_message.replace(substring, "", 1)
        concealed_message += substring[::-1]
        print(concealed_message)

    else:
        print("error")

    return concealed_message


def change_all(concealed_message, substring, replacement):
    concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)

    return concealed_message


# Inputs and logic loop
concealed_message = input()

while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        break

    if "InsertSpace" in command:
        index = int(command[1])
        concealed_message = insert_space(concealed_message, index)

    elif "Reverse" in command:
        substring = command[1]
        concealed_message = reverse(concealed_message, substring)

    elif "ChangeAll" in command:
        substring, replacement = command[1], command[2]
        concealed_message = change_all(concealed_message, substring, replacement)

# Final printout
print(f"You have a new text message: {concealed_message}")
