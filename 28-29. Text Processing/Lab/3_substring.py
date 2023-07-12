key = input()
string = input()

while key in string:
    string = string.replace(key, "")

print(string)