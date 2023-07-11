courses = {}

while True:
    line = input()

    if line == "end":
        break

    course, student = line.split(" : ")

    if course not in courses.keys():
        courses[course] = [student]
    else:
        courses[course].append(student)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
