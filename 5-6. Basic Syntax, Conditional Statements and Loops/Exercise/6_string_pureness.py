# n = int(input('Give me a number:'))
n = int(input())

no_no_symbols = [',', '.', '_']

for i in range(n):
    # string = str(input("Give me a string:"))
    string = str(input())
    impure_flag = False
    for j in string:
        if j in no_no_symbols:
            impure_flag = True
    if not impure_flag:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')