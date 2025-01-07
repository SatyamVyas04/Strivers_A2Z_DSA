import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        min_heap = [(0, 0, 0)]

        while min_heap:
            current_effort, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols - 1:
                return current_effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_effort = max(current_effort, abs(
                        grid[r][c] - grid[nr][nc]))

                    if next_effort < effort[nr][nc]:
                        effort[nr][nc] = next_effort
                        heapq.heappush(min_heap, (next_effort, nr, nc))

        return -1

# Link: https://leetcode.com/problems/path-with-minimum-effort/submissions/1501033360/
