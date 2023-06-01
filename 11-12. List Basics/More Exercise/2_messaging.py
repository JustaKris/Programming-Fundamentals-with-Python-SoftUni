number_list = input().split()
text = input()

message = ""

for number in number_list:
    digit_sum = sum([int(digit) for digit in number])
    index = digit_sum % len(text)

    message += text[index]
    text = text[:index] + text[index + 1:]

print(message)
