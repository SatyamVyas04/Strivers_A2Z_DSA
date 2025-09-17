class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]

        # reaching right-most ends -> only 1 way
        for i in range(n):
            grid[0][i] = 1

        # reaching bottom-most ends -> only 1 way
        for j in range(m):
            grid[j][0] = 1

        # realised to reach a point, we need top + left
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]

# Link: https://leetcode.com/problems/unique-paths/
