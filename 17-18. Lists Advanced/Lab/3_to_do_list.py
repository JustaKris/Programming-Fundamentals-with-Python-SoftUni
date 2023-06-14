task = (input())

tasks = []
while task != "End":
    tasks.append(task)
    task = (input())

sorted_tasks = sorted(tasks, key=lambda x: int(x.split("-")[0]))
tasks_final = [task.split("-")[1] for task in sorted_tasks]

print(tasks_final)

