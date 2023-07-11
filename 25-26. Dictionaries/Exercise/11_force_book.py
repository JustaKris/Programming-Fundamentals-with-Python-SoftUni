force_sides = {}

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        force_side, force_user = line.split(" | ")

        if force_side not in force_sides:
            force_sides[force_side] = []

        if force_user not in [user for users in force_sides.values() for user in users]:
            force_sides[force_side].append(force_user)

    elif " -> " in line:
        force_user, force_side = line.split(" -> ")
        user_current_side = None

        for side, users in force_sides.items():
            if force_user in users:
                user_current_side = side
                break

        if user_current_side:
            force_sides[user_current_side].remove(force_user)

        if force_side not in force_sides:
            force_sides[force_side] = []

        force_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force_side, force_users in force_sides.items():
    if force_users:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")
