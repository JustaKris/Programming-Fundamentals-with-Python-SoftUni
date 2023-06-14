conference_rooms = int(input())

insufficient_chairs = False
free_chairs = 0
for room in range(1, conference_rooms + 1):
    # print(room)
    chairs, visitors = input().split()
    visitors = int(visitors)
    if len(chairs) < visitors:
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
        insufficient_chairs = True
    else:
        free_chairs += len(chairs) - visitors

if not insufficient_chairs:
    print(f"Game On, {free_chairs} free chairs left")

