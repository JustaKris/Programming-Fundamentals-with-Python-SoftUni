strings = input().split()

repeated_strings = []
for string in strings:
    repeated_strings.append(string * len(string))

print(*repeated_strings, sep="")