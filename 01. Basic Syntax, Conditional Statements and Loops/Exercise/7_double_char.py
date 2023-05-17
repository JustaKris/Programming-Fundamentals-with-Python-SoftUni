# string = str(input("Give me a string:"))
string = str(input())

while string != 'End':
    if string != 'SoftUni':
        doubled_string = ''
        for character in string:
            doubled_string += character*2
        print(doubled_string)
        # string = str(input("Give me another string:"))
    string = str(input())
