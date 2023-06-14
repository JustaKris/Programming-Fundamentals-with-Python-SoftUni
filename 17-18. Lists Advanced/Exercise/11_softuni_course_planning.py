def add_lesson(lessons, lesson_title):
    if lesson_title not in lessons:
        lessons.append(lesson_title)
    return lessons


def insert_lesson(lessons, lesson_title, index):
    if lesson_title not in lessons:
        lessons.insert(index, lesson_title)
    return lessons


def remove_lesson(lessons, lesson_title):
    if lesson_title in lessons:
        lesson_title_index = lessons.index(lesson_title)
        if lesson_title_index + 1 in range(len(lessons)):
            if "Exercise" in lessons[lesson_title_index + 1]:
                lessons.pop(lesson_title_index + 1)
        lessons.remove(lesson_title)
    return lessons


def swap_lesson(lessons, lesson_title, other_lesson_title):
    if lesson_title in lessons and other_lesson_title in lessons:
        # Get lesson indexes
        lesson_index = lessons.index(lesson_title)
        other_lesson_index = lessons.index(other_lesson_title)

        # Check for exercises
        lesson_has_exercise = False
        other_lesson_has_exercise = False
        if lesson_index + 1 in range(len(lessons)):
            lesson_has_exercise = "Exercise" in lessons[lesson_index + 1]
        if other_lesson_index in range(len(lessons)):
            other_lesson_has_exercise = "Exercise" in lessons[other_lesson_index + 1]

        # Swap Lessons
        lessons[lesson_index], lessons[other_lesson_index] = lessons[other_lesson_index], lessons[lesson_index]

        # Handle Exercises swap cases
        if lesson_has_exercise and other_lesson_has_exercise:
            lessons[lesson_index + 1], lessons[other_lesson_index + 1] = lessons[other_lesson_index + 1], lessons[
                lesson_index + 1]
        elif not lesson_has_exercise and other_lesson_has_exercise:
            lessons.insert(lesson_index + 1, lessons.pop(other_lesson_index + 1))
        elif lesson_has_exercise and not other_lesson_has_exercise:
            lessons.insert(other_lesson_index + 1, lessons.pop(lesson_index + 1))
    return lessons


def exercise(lessons, lesson_title):
    if lesson_title in lessons and f"{lesson_title}-Exercise" not in lessons:
        lessons.insert(lessons.index(lesson_title) + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in lessons:
        lessons.append(lesson_title)
        lessons.append(f"{lesson_title}-Exercise")
    return lessons


lessons = input().split(", ")
command = input()

while command != "course start":
    # Setting up possible variables
    command = command.split(":")
    action, lesson_title = command[0], command[1]
    if action == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert_lesson(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif action == "Swap":
        other_lesson_title = command[2]
        lessons = swap_lesson(lessons, lesson_title, other_lesson_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input()

# Printouts
for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")
