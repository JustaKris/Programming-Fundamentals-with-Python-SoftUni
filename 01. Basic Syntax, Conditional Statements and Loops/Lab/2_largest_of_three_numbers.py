# first_num = 6
# second_num = 8
# third_num = 5

print("I will print the largest of 3 number you give me")
first_num = int(input("Give me the first number:"))
second_num = int(input("Give me the first second:"))
third_num = int(input("Give me the third number:"))

if first_num > second_num and first_num > third_num:
    print(first_num)
elif second_num > first_num and second_num > third_num:
    print(second_num)
else:
    print(third_num)