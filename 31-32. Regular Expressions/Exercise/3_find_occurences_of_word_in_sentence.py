import re

line = input().lower()
word = input().lower()

regex = r'\b' + word + r'\b'
words = re.findall(regex, line)

print(len(words))
