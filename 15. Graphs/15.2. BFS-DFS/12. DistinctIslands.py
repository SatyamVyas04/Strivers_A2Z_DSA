def distinctIsland(grid, m, n):
    # Depth-first search function to explore the island
    def depth_first_search(i: int, j: int, move: int):
        grid[i][j] = 0  # Marking the visited cell as '0' to avoid revisiting
        path.append(str(move))  # Add the move direction to path
        # Possible movements in the four directions: up, right, down, left
        directions = (-1, 0, 1, 0, -1)
        # Iterating over the four possible directions
        for h in range(4):
            # Calculate new cell's coordinates
            x, y = i + directions[h], j + directions[h+1]
            # Check if the new cell is within bounds and is part of an island
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                depth_first_search(x, y, h+1)
        # Add the reverse move to path to differentiate shapes
        path.append(str(-move))

    # Set to store unique paths that represent unique island shapes
    paths = set()
    # Temporary list to store the current island's path shape
    path = []
    # Iterate over every cell in the grid
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value:  # Check if the cell is part of an island
                depth_first_search(i, j, 0)  # Start DFS from this cell
                # Add the path shape to the set of paths
                paths.add("".join(path))
                path.clear()  # Clear the path for next island
                # print(paths)  # Debugging

    # Number of distinct islands is the number of unique path shapes
    return len(paths)

# Link: https://www.naukri.com/code360/problems/distinct-islands_630460?leftPanelTabValue=PROBLEM
