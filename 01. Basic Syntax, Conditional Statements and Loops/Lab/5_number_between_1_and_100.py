num = float(input("Give me a number and I will tell you when it's between 1 and 100:"))
while num < 1 or num > 100:
    num = float(input("Give me another number:"))
print(f"The number {num} is between 1 and 100")