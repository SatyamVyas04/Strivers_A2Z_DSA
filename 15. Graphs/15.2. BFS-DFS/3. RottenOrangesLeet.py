from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_positions = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_positions.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        while rotten_positions:
            new_rotten_positions = []
            for i, j in rotten_positions:
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        new_rotten_positions.append((x, y))

            rotten_positions = new_rotten_positions
            if rotten_positions:
                minutes += 1
        return -1 if any(1 in row for row in grid) else minutes

# Link: https://leetcode.com/problems/rotting-oranges/
