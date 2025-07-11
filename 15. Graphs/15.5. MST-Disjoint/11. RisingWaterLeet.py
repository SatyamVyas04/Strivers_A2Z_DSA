import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minheap = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visit.add((0, 0))
        while minheap:
            t, r, c = heapq.heappop(minheap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minheap, [max(t, grid[nr][nc]), nr, nc])
        return -1

# Link: https://leetcode.com/problems/swim-in-rising-water/submissions/1503398533/
