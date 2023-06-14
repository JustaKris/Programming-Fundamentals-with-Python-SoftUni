import math

first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
student_questions = int(input())

total_work_capacity = sum([first_employee_capacity, second_employee_capacity,third_employee_capacity])

working_hours = student_questions / total_work_capacity
breaks = working_hours / 4

total_hours = math.ceil(working_hours + breaks)

print(f"Time needed: {total_hours}h.")

# hours_needed = 0
# hours_since_break = 0
#
# while student_questions > 0:
#     if hours_since_break == 3:
#         hours_needed += 2
#         hours_since_break = 0
#     else:
#         hours_needed += 1
#         hours_since_break += 1
#     student_questions -= sum([first_employee_capacity, second_employee_capacity,third_employee_capacity])
#
# print(f"Time needed: {hours_needed}h.")
