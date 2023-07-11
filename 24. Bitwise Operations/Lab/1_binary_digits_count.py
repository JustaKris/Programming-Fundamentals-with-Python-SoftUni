number = 20
digit = 0
count = 0

while number > 0:
    remainder = number % 2

    if remainder == digit:
        count += 1

    number //= 2

print(count)
