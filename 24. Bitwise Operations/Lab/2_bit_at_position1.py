def solve(number):
    mask = 1 << 1
    bit = number & mask
    result = bit >> 1
    print(result)


solve(2)
solve(13)
