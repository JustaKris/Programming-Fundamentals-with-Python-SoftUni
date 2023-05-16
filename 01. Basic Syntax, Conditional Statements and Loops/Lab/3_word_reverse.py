word = str(input("Give me word that I will reverse:"))

# print(word[::-1])

# Alternative solution using a for loop
reversed_word = ""

for i in range(len(word)-1,-1,-1):
    reversed_word += word[i]
print(reversed_word)