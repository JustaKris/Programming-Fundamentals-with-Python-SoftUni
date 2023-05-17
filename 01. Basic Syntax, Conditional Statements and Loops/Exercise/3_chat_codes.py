# number_count = int(input("How many numbers do we have:"))
number_count = int(input())

for numbers in range(number_count):
    # number = int(input("Give me a number:"))
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print('GREAT!')
    else:
        print("Bye.")