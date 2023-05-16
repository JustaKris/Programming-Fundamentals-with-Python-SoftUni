n = int(input("Number count:"))

for i in range(n):
    number = int(input("Give me a number:"))
    if not number % 2 == 0:
        print(f"{number} is odd")
        break
else:
    print("All numbers are even.")

