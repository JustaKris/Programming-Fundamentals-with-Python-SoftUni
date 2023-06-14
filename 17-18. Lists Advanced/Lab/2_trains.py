wagons = [0 for i in range(int(input()))]

command = input()
while command != "End":
    if "add" in command:
        _, people = command.split()
        wagons[-1] += int(people)
    elif "insert" in command:
        _, index, people = command.split()
        wagons[int(index)] += int(people)
    elif 'leave' in command:
        _, index, people = command.split()
        wagons[int(index)] -= int(people)
    command = input()

print(wagons)
