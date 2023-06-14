string = input()

letters = [letter for letter in string if not letter.isdigit()]
digits = [int(element) for element in string if element.isdigit()]
take_list = [digits[i] for i in range(len(digits)) if i % 2 == 0]
skip_list = [digits[i] for i in range(len(digits)) if i % 2 != 0]

result = ""
skip_count = 0

for i in range(len(take_list)):
    take_count = take_list[i]
    skip_count += skip_list[i]

    result += "".join(letters[:take_count])
    letters = letters[take_count + skip_count:]
    skip_count = 0

print(result)
