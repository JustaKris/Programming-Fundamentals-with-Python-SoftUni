# input_string = input()
#
# strings = []
# counter = 0
# for i in range(len(input_string)):
#     if not input_string[i].isdigit():
#         counter += 1
#     else:
#         strings.append(input_string[i - counter: i + 1])
#         counter = 0
#
# final_string = ""
# for element in strings:
#     string = element[:(len(element) - 1)]
#     number = int(element[-1])
#     final_string += string.upper() * number
#
# unique_symbols_count = len(set(final_string))
# print(f"Unique symbols used: {unique_symbols_count}")
# print(final_string)

text = input().upper()
unique_symbols = ""
current_symbol = ""
repetitions = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else:
        for next_symbols_index in range(index, len(text)):
            if not text[next_symbols_index].isdigit():
                break
            repetitions += text[next_symbols_index]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
