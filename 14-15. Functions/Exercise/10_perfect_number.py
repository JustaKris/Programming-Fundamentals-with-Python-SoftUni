def perfect_number_check(number):
    divisors = [num for num in range(1, number) if number % num == 0]
    if number == (sum(divisors) + number) / 2:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number_check(number))
