from typing import List
from queue import Queue


class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        queue = [0]
        visited = set()
        ans = []

        while queue:
            current = queue.pop(0)
            if current not in visited:
                ans.append(current)

            visited.add(current)
            for nei in adj[current]:
                if nei not in visited:
                    queue.append(nei)

        return ans

# Link: https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
