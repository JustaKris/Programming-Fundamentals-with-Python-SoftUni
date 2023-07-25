import re

# Reading input string
string = input()

# Getting the cool threshold
cool_threshold = 0.0
for symbol in string:
    if symbol.isdigit():
        if cool_threshold > 0:
            cool_threshold *= int(symbol)
        else:
            cool_threshold = int(symbol)

# Capturing all emojis and storing them in a dictionary with their coolness
# pattern = r'([\*\:]{2})([A-Z][a-z]{2,}){1,}\1{1}'
pattern = r'([\*\:]{2})([A-Z])([a-z]{2,})\1'
matches = re.finditer(pattern, string)

emojis_dict = {emoji.group(0): 0.0 for emoji in matches}
for emoji in emojis_dict.keys():
    coolness = 0.0
    for letter in emoji[1:-2]:
        coolness += ord(letter)
    emojis_dict[emoji] = coolness

# Printouts
print(f"Cool threshold: {cool_threshold:.0f}")
print(f"{len(emojis_dict.keys())} emojis found in the text. The cool ones are:")
for emoji, coolness in emojis_dict.items():
    if coolness >= cool_threshold:
        print(f"{emoji} ")
