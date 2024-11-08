from typing import List
from collections import deque


class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        original_color = grid[sr][sc]

        # If the color is already the target color, no need to proceed
        if original_color == color:
            return grid

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(sr, sc)])
        grid[sr][sc] = color

        while queue:
            cr, cc = queue.popleft()

            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc

                # Check if the neighbor is within bounds and has the original color
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == original_color:
                    grid[nr][nc] = color
                    queue.append((nr, nc))

        return grid

# Link: https://leetcode.com/problems/flood-fill/description/
