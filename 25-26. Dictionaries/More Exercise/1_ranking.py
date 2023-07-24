def main():
    contests = {}
    submissions = {}

    # Step 1: Read valid contests and passwords
    while True:
        contest_info = input()
        if contest_info == "end of contests":
            break
        contest, password = contest_info.split(":")
        contests[contest] = password

    # Step 2: Read submissions and store user data with points for each contest
    while True:
        submission_info = input()
        if submission_info == "end of submissions":
            break
        contest, password, username, points = submission_info.split("=>")
        points = int(points)

        if contest in contests and contests[contest] == password:
            if username not in submissions:
                submissions[username] = {}
            if contest not in submissions[username] or points > submissions[username][contest]:
                submissions[username][contest] = points

    # Step Practice exam 1: Calculate total points for each user
    user_points = {}
    for username, contest_points in submissions.items():
        user_points[username] = sum(contest_points.values())

    # Step 4: Find the user with the highest total points
    best_candidate = max(user_points, key=user_points.get)
    total_points = user_points[best_candidate]

    # Step 5: Print the best candidate and sorted user data
    print(f"Best candidate is {best_candidate} with total {total_points} points.")
    print("Ranking:")
    sorted_users = sorted(submissions.keys())
    for user in sorted_users:
        print(user)
        for contest, points in sorted(submissions[user].items(), key=lambda x: (-x[1], x[0])):
            print(f"#  {contest} -> {points}")


if __name__ == "__main__":
    main()
