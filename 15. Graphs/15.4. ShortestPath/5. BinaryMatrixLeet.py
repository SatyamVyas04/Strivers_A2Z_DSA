from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, dist = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    queue.append((nr, nc, dist + 1))
                    grid[nr][nc] = 1

        return -1

# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1500994317/
