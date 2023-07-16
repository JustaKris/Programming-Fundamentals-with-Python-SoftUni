string = input()

final_string = ""

previous_symbol = ""

for char in string:
    if char == previous_symbol:
        continue
    else:
        previous_symbol = char
        final_string += char

print(final_string)
