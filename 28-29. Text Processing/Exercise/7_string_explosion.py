string = input()

final_string = ""
explosion_str = 0
for index in range(len(string)):
    if explosion_str > 0 and string[index] != ">":
        explosion_str -= 1
    elif string[index] == ">":
        final_string += string[index]
        explosion_str += int(string[index + 1])
    else:
        final_string += string[index]

print(final_string)
