words = input().split()

dictionary = {}
for word in words:
    lower_word = word.lower()
    if lower_word not in dictionary.keys():
        dictionary[lower_word] = 1
    else:
        dictionary[lower_word] += 1

result = []
for k, v in dictionary.items():
    if v % 2 != 0:
        result.append(k)

print(*result, sep=" ")
