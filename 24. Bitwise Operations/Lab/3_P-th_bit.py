def solve(number, position):
    mask = 1 << position
    result = number & mask
    lsb = result >> position
    print(lsb)


solve(2145, 5)
