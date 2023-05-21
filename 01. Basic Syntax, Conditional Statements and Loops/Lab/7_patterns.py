stars = int(input())

for i in range(1, stars+1):
    for j in range(0, i):
        print("*", end='')
    print()

for i in range(stars-1, 0, -1):
    for j in range(0, i):
        print("*", end='')
    print()
