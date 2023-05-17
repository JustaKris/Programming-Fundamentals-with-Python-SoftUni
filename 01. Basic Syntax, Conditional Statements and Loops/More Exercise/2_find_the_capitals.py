string = str(input())

indexes = []
for i in range(len(string)):
    if string[i] == string[i].upper():
        indexes.append(i)

print(indexes)