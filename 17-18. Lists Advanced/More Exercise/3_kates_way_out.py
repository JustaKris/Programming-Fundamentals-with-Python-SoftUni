def find_exit(maze):
    # Find the initial position of Kate
    start_row, start_col = -1, -1
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "k":
                start_row, start_col = row, col
                break
        if start_row != -1:
            break

    # Perform depth-first search
    num_moves = dfs(maze, start_row, start_col)
    if num_moves == -1:
        print("Kate cannot get out")
    else:
        print("Kate got out in", num_moves, "moves")


def dfs(maze, row, col):
    # Check if the current position is outside the maze
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[row]):
        return -1

    # Check if Kate has found a way out
    if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[row]) - 1:
        return 0

    # Check if the current position is a wall or has already been visited
    if maze[row][col] == "#" or maze[row][col] == "v":
        return -1

    # Mark the current position as visited
    maze[row][col] = "v"

    # Try moving in all four directions
    moves = []
    moves.append(dfs(maze, row - 1, col))  # Move up
    moves.append(dfs(maze, row + 1, col))  # Move down
    moves.append(dfs(maze, row, col - 1))  # Move left
    moves.append(dfs(maze, row, col + 1))  # Move right

    # Find the longest path
    longest_path = max(m for m in moves if m != -1)
    if longest_path != -1:
        return longest_path + 1

    return -1


# Read the number of rows in the maze
num_rows = int(input())

# Read the maze itself
maze = []
for _ in range(num_rows):
    row = list(input().strip())
    maze.append(row)

# Find Kate's way out
find_exit(maze)
