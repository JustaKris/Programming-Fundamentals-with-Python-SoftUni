def palindrome_check(list_of_numbers):
    for num in list_of_numbers:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")

palindrome_check(numbers)
