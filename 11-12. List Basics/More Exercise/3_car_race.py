numbers = input().split()
numbers = [int(num) for num in numbers]

half_point_rounded = len(numbers) // 2

left_car_values = numbers[:half_point_rounded]
right_car_values = numbers[half_point_rounded + 1:]
right_car_values = right_car_values[::-1]

finish = numbers[half_point_rounded]

left_zeroes = left_car_values.count(0)
right_zeroes = right_car_values.count(0)

left_car_time = 0
right_car_time = 0

for element in left_car_values:
    if element == 0:
        left_car_time = left_car_time * 0.8
    else:
        left_car_time += element

for element in right_car_values:
    if element == 0:
        right_car_time = right_car_time * 0.8
    else:
        right_car_time += element

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
elif right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")


# ChatGPT solution
# def announce_winner(times):
#     time_list = [float(time) for time in times.split()]
#     middle_index = len(time_list) // 2
#
#     left_total_time = sum(time_list[:middle_index])
#     right_total_time = sum(time_list[middle_index + 1:])
#
#     if 0 in time_list:
#         if left_total_time > 0:
#             left_total_time *= 0.8
#         if right_total_time > 0:
#             right_total_time *= 0.8
#
#     winner = "left" if left_total_time < right_total_time else "right"
#     total_time = min(left_total_time, right_total_time)
#
#     print(f"The winner is {winner} with total time: {total_time:.1f}")
#
#
# input_times = input()
# announce_winner(input_times)
