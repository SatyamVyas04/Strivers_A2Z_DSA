# Island Perimeter
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                curr = grid[row][col]
                if curr:
                    ans += 4
                    if row > 0:
                        if grid[row - 1][col]:
                            ans -= 1
                    if row < rows - 1:
                        if grid[row + 1][col]:
                            ans -= 1
                    if col > 0:
                        if grid[row][col - 1]:
                            ans -= 1
                    if col < cols - 1:
                        if grid[row][col + 1]:
                            ans -= 1
        return ans
