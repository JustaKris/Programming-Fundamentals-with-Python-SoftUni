food = float(input())
hay = float(input())
cover = float(input())
guinea_pig_weight = float(input())

for day in range(1, 31):
    food -= 0.3
    # guinea_pig_weight += 0.3

    if day % 2 == 0:
        hay -= food * 0.05

    if day % 3 == 0:
        cover -= guinea_pig_weight / 3

if food < 0 or hay < 0 or cover < 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")

