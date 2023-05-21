n_people = int(input())
elevator_capacity = int(input())

courses_full = n_people // elevator_capacity
remainder = n_people % elevator_capacity

# if n_people <= elevator_capacity:
#     print("All the persons fit inside the elevator.\nOnly one course is needed.")
#
# else:
#     print(f"{courses_full} courses * {elevator_capacity} people")
#     if remainder:
#         print(f"+ 1 course * {remainder} persons")



# bugged solution

if n_people <= elevator_capacity:
    print(1)

else:
    if remainder:
        print(courses_full + 1)
    else:
        print(courses_full)