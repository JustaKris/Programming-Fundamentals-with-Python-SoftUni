sequence1 = input().split(", ")
sequence2 = input().split(", ")

final_sequence = []

for element1 in sequence1:
    for element2 in sequence2:
        if element1 in element2:
            final_sequence.append(element1)
            break

print(final_sequence)

# List comprehension approach
# final_sequence2 = [first_word for first_word in sequence1 if any(first_word in second_word for second_word in sequence2)]
# print(final_sequence2)
