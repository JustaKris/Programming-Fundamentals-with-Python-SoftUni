strings = input().split()

result = 0
for string in strings:
    # Dividing the strings into the required components
    first_letter = string[0]
    second_letter = string[-1]
    number = int(string[1:len(string) - 1])

    # First letter calculations
    if first_letter.isupper():
        number /= ord(first_letter) - 64
    else:
        number *= ord(first_letter) - 96

    # Second letter calculations
    if second_letter.isupper():
        number -= ord(second_letter) - 64
    else:
        number += ord(second_letter) - 96

    result += number

print(f"{result:.2f}")
