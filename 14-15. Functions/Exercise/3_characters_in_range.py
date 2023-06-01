def ascii_range(first_character, second_character):
    """
    Returns a list of all ascii characters between first_character and second_character
    """
    ascii_list = []
    for i in range(ord(first_character) + 1, ord(second_character)):
        ascii_list.append(chr(i))
    return ascii_list


input_character_1 = input()
input_character_2 = input()

ascii_list = ascii_range(input_character_1, input_character_2)

for item in ascii_list:
    print(item, end=" ")
