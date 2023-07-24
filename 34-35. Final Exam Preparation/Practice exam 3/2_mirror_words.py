import re

# Reading input string
string = input()

# Capturing all strings which fit the required pattern
pattern = r"([@#])(?P<first_word>[A-Za-z]{3,})\1{2}(?P<second_word>[A-Za-z]{3,})\1"
matches = re.finditer(pattern, string)

# Building mirror_words dict and counting total matches
mirror_words = {}
match_count = 0
for match in matches:
    word_combo = match.groupdict()
    match_count += 1
    if match["first_word"] == match["second_word"][::-1]:
        mirror_words[match["first_word"]] = match["second_word"]

# Printing results
if mirror_words:
    print(f"{match_count} word pairs found!")
    print("The mirror words are:")

    combined_words = []
    for key, value in mirror_words.items():
        word_pair = key + " <=> " + value
        combined_words.append(word_pair)
    print(*combined_words, sep=", ")
else:
    if match_count:
        print(f"{match_count} word pairs found!")
    else:
        print("No word pairs found!")
    print("No mirror words!")
