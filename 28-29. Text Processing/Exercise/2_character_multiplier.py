def character_multiplier(strings):
    result = 0

    string_lengths = [len(string) for string in strings]
    min_length = min(string_lengths)
    max_length = max(string_lengths)

    for i in range(min_length):
        result += ord(strings[0][i]) * ord(strings[1][i])

    if len(strings[0]) > len(strings[1]):
        for i in range(min_length, max_length):
            result += ord(strings[0][i])
    else:
        for i in range(min_length, max_length):
            result += ord(strings[1][i])

    return result


strings = input().split()
print(character_multiplier(strings))
