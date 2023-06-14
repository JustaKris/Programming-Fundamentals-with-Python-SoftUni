# people_in_queue = int(input())
# lift = [int(car) for car in input().split()]
#
# for i in range(people_in_queue):
#     for j in range(len(lift)):
#         if sum(lift) / len(lift) == 4:
#             break
#         elif lift[j] < 4 and people_in_queue:
#             lift[j] += 1
#             people_in_queue -= 1
#
# if people_in_queue:
#     print(f"There isn't enough space! {people_in_queue} people in a queue!")
# elif sum(lift) / len(lift) != 4:
#     print("The lift has empty spots!")
# print(" ".join([str(car) for car in lift]))


# ChatGPT solution

people_waiting = int(input())
lift_state = [int(x) for x in input().split()]

full_capacity = len(lift_state) * 4
total_people = sum(lift_state)

while people_waiting > 0 and total_people < full_capacity:
    for i in range(len(lift_state)):
        while lift_state[i] < 4 and people_waiting > 0:
            lift_state[i] += 1
            people_waiting -= 1
            total_people += 1
            if total_people == full_capacity or people_waiting == 0:
                break

if people_waiting == 0 and total_people < full_capacity:
    print("The lift has empty spots!")
    print(' '.join(str(x) for x in lift_state))
elif people_waiting > 0 and total_people >= full_capacity:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(' '.join(str(x) for x in lift_state))
else:
    print(' '.join(str(x) for x in lift_state))
