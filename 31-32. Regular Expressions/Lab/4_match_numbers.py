import re


def match_numbers(text):
    regex = r'(?:(?<=^)|(?<=\s))-?\d+(?:\.\d+)?(?=\s|$)'
    numbers = re.findall(regex, text)
    return numbers


# Example usage
text = input()
numbers = match_numbers(text)
print(" ".join(numbers))
