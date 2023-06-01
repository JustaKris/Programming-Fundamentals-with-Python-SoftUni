def smallest_of_three(num_1, num_2, num_3):
    return min([num_1, num_2, num_3])


# Lambda approach
smallest_of_three_lambda = lambda num_1, num_2, num_3: min([num_1, num_2, num_3])

input_num_1 = int(input())
input_num_2 = int(input())
input_num_3 = int(input())

print(smallest_of_three(input_num_1, input_num_2, input_num_3))