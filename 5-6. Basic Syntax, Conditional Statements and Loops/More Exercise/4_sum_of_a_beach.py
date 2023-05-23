# string = 'gOfIshsunesunFiSh'
string = str(input())

words_to_count = ['SAND', 'WATER', 'FISH', 'SUN']

count = 0
for word in words_to_count:
    count += len(string.upper().split(word))-1
print(count)