import re

phone_numbers = input()

regex = "\\+359[ -]2[ -]\\d{Practice exam 1}[ -]\\d{4}\\b"
matches = re.findall(regex, phone_numbers)
print(", ".join(matches))
