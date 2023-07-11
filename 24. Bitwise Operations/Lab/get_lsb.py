def solve(number):
    mask = 1

    # LSB stands for LEast Significant Bit which is the left mose bit of a binary number
    lsb = number % mask

    print(lsb)


solve(20)
