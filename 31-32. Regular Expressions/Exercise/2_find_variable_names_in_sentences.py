import re

line = input()

regex = r'\b_([A-Za-z]+)\b'
variable_names = re.findall(regex, line)

print(*variable_names, sep=",")
