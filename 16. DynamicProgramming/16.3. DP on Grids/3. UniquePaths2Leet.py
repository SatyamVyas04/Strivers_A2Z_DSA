from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0 for _ in range(n)] for _ in range(m)]

        # Starting cell
        if obstacleGrid[0][0] == 1:
            return 0
        grid[0][0] = 1

        # Fill first column
        for row in range(1, m):
            if obstacleGrid[row][0] == 1:
                grid[row][0] = 0
            else:
                grid[row][0] = grid[row - 1][0]

        # Fill first row
        for col in range(1, n):
            if obstacleGrid[0][col] == 1:
                grid[0][col] = 0
            else:
                grid[0][col] = grid[0][col - 1]

        # Fill the rest
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

        return grid[-1][-1]

# Link: https://leetcode.com/problems/unique-paths-ii/submissions/1782452691/
