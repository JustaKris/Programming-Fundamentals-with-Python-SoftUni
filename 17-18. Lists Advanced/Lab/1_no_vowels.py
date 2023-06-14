def remove_vowels(string):
    vowels = ['a', 'o', 'u', 'e', 'i']
    clean_string = [letter for letter in string if letter.lower() not in vowels]
    return "".join(clean_string)


string = input()
print(remove_vowels(string))
