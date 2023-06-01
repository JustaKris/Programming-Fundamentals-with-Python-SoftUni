def factorial_division(num1, num2):
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    factorial1 = factorial(num1)
    factorial2 = factorial(num2)

    division_result = factorial1 / factorial2

    return f"{division_result:.2f}"


num1 = int(input())
num2 = int(input())

print(factorial_division(num1, num2))
