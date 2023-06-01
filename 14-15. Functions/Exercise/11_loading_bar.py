def loading_bar(number):
    number //= 10
    if number < 10:
        print(f"{number*10}% [" + "%" * number + "." * (10 - number) + "]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


number = int(input())
loading_bar(number)

