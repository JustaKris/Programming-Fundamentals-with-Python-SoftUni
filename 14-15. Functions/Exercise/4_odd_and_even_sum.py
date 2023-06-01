def odd_even_sum(string):
    odd_sum = 0
    even_sum = 0
    for num in string:
        if num.isdigit():
            if int(num) % 2 == 0:
                even_sum += int(num)
            else:
                odd_sum += int(num)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


input_string = input()

print(odd_even_sum(input_string))
