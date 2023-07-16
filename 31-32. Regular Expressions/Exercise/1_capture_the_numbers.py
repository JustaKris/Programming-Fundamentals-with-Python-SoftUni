import re

numbers = []

string = input()
while string:
    numbers += re.findall(r'\d+', string)
    string = input()

print(*numbers, sep=" ")

# ChatGPT

# import re
#
#
# def extract_numbers_from_string(input_string):
#     # Use regular expression to find all sequences of digits in the input string
#     numbers = re.findall(r'\d+', input_string)
#     return numbers
#
#
# def main():
#     extracted_numbers = []
#
#     while True:
#         try:
#             # Read input line by line until EOF (Ctrl+D or Ctrl+Z)
#             line = input()
#             numbers = extract_numbers_from_string(line)
#             extracted_numbers.extend(numbers)
#         except EOFError:
#             # Break the loop when the end of input is reached
#             break
#
#     # Join the extracted numbers into a single line with space separation
#     output = " ".join(extracted_numbers)
#     print(output)
#
#
# if __name__ == "__main__":
#     main()
