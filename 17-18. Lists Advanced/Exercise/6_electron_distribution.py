def electron_distribution(num_electrons: int) -> list:
    shells = []  # List to store the filled shells

    n = 1  # Shell position
    while num_electrons > 0:
        max_electrons = 2 * n ** 2  # Maximum number of electrons in the current shell

        if num_electrons >= max_electrons:
            shells.append(max_electrons)
            num_electrons -= max_electrons
        else:
            shells.append(num_electrons)
            num_electrons = 0

        n += 1  # Move to the next shell

    return shells


electrons = int(input())
print(electron_distribution(electrons))
