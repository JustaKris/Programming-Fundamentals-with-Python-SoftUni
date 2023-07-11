def solve(number, position):
    mask = ~(1 << position)
    result = number & mask

    print(result)


solve(1313, 5)
