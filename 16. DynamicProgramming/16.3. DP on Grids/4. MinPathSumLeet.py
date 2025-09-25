from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                elif r == 0:
                    grid[r][c] += grid[r][c-1]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])

        return grid[-1][-1]

# Link: https://leetcode.com/problems/minimum-path-sum/
