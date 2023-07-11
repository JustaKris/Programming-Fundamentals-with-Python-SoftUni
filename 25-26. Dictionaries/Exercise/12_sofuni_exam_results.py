submissions = {}
languages = {}

while True:
    line = input()
    if line == "exam finished":
        break

    if "-banned" in line:
        username, _ = line.split("-banned")
        if username in submissions:
            del submissions[username]
    else:
        username, language, points = line.split("-")
        points = int(points)

        if username not in submissions:
            submissions[username] = {}

        if language not in submissions[username] or points > submissions[username][language]:
            submissions[username][language] = points

        if language not in languages:
            languages[language] = 0
        languages[language] += 1

print("Results:")
for username, user_submissions in submissions.items():
    max_points = max(user_submissions.values())
    print(f"{username} | {max_points}")

print("Submissions:")
for language, count in languages.items():
    print(f"{language} - {count}")
