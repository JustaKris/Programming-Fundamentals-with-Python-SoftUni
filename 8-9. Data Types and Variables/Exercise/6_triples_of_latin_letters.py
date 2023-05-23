number = int(input())

for i in range(97, number + 97):
    first_letter = str(chr(i))
    for j in range(97, number + 97):
        second_letter = str(chr(j))
        for k in range(97, number + 97):
            third_letter = str(chr(k))
            print(first_letter + second_letter + third_letter)