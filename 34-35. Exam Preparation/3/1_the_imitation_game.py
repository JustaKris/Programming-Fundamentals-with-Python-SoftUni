encrypted_message = input()
command = input().split("|")

while command[0] != "Decode":

    if command[0] == "Move":
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]

    elif command[0] == "Insert":
        index, value = int(command[1]), command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input().split("|")

print(f"The decrypted message is: {encrypted_message}")
