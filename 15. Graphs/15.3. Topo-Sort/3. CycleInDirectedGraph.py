from typing import List
from collections import deque


class Solution:
    def isCyclic(self, n: int, adj: List[List[int]]) -> bool:
        in_degree = [0] * n

        for i in range(n):
            for node in adj[i]:
                in_degree[node] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return len(result) != n

# Intuition: Kahn's algorithm won't let me process/add independent nodes to the queue, since their in-degree can only be satisfied by themselves. So I just ran the algorithm and compared the length of the result with the number of nodes.
# Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1