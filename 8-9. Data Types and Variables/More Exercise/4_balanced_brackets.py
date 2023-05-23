number_of_inputs = int(input())

balanced = True
last_bracket = ''
brackets_check = ['(', ')']
left_bracket_counter = 0
right_bracket_counter = 0
for i in range(number_of_inputs):

    current_input = str(input())
    if current_input in brackets_check:

        if current_input != last_bracket:
            last_bracket = current_input
        else:
            balanced = False
            break

        if current_input == brackets_check[0]:
            left_bracket_counter += 1
        else:
            right_bracket_counter += 1

if left_bracket_counter == right_bracket_counter and balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
