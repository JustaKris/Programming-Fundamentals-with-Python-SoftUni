def dfs(board, i, j):
    # Check if the current position is within the board boundaries
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return 0

    # Check if the current position is a dot
    if board[i][j] != '.':
        return 0

    count = 1
    # Mark the current position as visited
    board[i][j] = '-'

    # Recursive calls for neighboring positions
    count += dfs(board, i + 1, j)  # Down
    count += dfs(board, i - 1, j)  # Up
    count += dfs(board, i, j + 1)  # Right
    count += dfs(board, i, j - 1)  # Left

    return count


# Read the number of rows
n = int(input())

# Read the board
board = []
for _ in range(n):
    row = input().split()
    board.append(row)

# Initialize the maximum count of connected dots
max_count = 0

# Iterate over each position on the board
for i in range(n):
    for j in range(len(board[i])):
        if board[i][j] == '.':
            # Calculate the count of connected dots starting from the current position
            count = dfs(board, i, j)
            # Update the maximum count if necessary
            max_count = max(max_count, count)

# Print the largest count of connected dots
print(max_count)
