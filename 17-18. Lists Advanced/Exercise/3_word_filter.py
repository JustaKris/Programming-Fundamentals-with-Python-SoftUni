input_list = input().split()

filtered_list = [word for word in input_list if len(word) % 2 == 0]

for word in filtered_list:
    print(word)
    