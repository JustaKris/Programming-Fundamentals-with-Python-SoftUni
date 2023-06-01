strings_list = input().split(" ")
shuffles = int(input())

for i in range(shuffles):
    # Split list
    input_list_a = strings_list[:len(strings_list) // 2]
    input_list_b = strings_list[len(strings_list) // 2::]
    # Save start and end values and pop before looping
    input_list_start = input_list_a[0]
    input_list_end = input_list_b[-1]

    input_list_a.pop(0)
    input_list_b.pop(len(input_list_b) - 1)

    shuffled_list = [input_list_start]
    for j in range(len(input_list_a)):
        shuffled_list.append(input_list_b[j])
        shuffled_list.append(input_list_a[j])
    shuffled_list.append(input_list_end)
     
    strings_list = shuffled_list

print(strings_list)

# ChatGPT solution
# cards = input().split()
# shuffles = int(input())
#
# deck_size = len(cards)
# half_size = deck_size // 2
#
# for _ in range(shuffles):
#     shuffled_deck = []
#     left_half = cards[:half_size]
#     right_half = cards[half_size:]
#
#     for i in range(half_size):
#         shuffled_deck.append(left_half[i])
#         shuffled_deck.append(right_half[i])
#
#     cards = shuffled_deck
#
# print(cards)
