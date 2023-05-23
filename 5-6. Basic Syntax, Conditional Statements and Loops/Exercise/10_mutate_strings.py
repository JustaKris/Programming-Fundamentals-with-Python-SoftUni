string_one = str(input())
string_two = str(input())

strings = [string_one] # Judge doesn't seem to be allowing me to print the first string I get which is not mentioned in the description
for i in range(1, len(string_one)+1):
    new_string = string_two[:i] + string_one[i:]
    if new_string in strings:
        continue
    strings.append(new_string)
    print(new_string)
