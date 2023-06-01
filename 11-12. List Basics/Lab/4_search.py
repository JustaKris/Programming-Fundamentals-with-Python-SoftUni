n = int(input())
word = input()

strings = []
for i in range(n):
    string = input()
    strings.append(string)
print(strings)

filtered_strings = []
for i in range(len(strings) - 1, -1, -1):
    if word not in strings[i]:
        strings.remove(strings[i])
print(strings)