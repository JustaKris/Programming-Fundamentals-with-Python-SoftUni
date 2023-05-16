number_count = int(input("How many numbers do we have:"))

for numbers in range(number_count):
    number = int(input("Give me a number:"))
    if number == 88:
        print('Hello')
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print('GREAT!')
    else:
        print("Bye")