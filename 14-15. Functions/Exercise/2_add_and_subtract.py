def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


# Lambda approach
sum_numbers_lambda = lambda num_1, num_2: num_1 + num_2
subtract_lambda = lambda num_1, num_2: num_1 - num_2

input_num_1 = int(input())
input_num_2 = int(input())
input_num_3 = int(input())

result_sum = sum_numbers(input_num_1, input_num_2)
result_subtract = subtract(result_sum, input_num_3)

print(result_subtract)
