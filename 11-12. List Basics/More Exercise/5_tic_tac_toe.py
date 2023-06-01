def check_winner(field):
    # Check rows
    for row in field:
        if row.count(1) == 3:
            return "First player won"
        elif row.count(2) == 3:
            return "Second player won"

    # Check columns
    for col in range(3):
        column = [field[row][col] for row in range(3)]
        if column.count(1) == 3:
            return "First player won"
        elif column.count(2) == 3:
            return "Second player won"

    # Check diagonals
    diagonal1 = [field[i][i] for i in range(3)]
    diagonal2 = [field[i][2-i] for i in range(3)]
    if diagonal1.count(1) == 3 or diagonal2.count(1) == 3:
        return "First player won"
    elif diagonal1.count(2) == 3 or diagonal2.count(2) == 3:
        return "Second player won"

    # No winner, check for empty spaces
    for row in field:
        if 0 in row:
            return "Draw!"

    # No winner and no empty spaces
    return "Draw!"


# Read the input
field = []
for _ in range(3):
    row = list(map(int, input().split()))
    field.append(row)

# Check the winner
result = check_winner(field)

# Print the result
print(result)