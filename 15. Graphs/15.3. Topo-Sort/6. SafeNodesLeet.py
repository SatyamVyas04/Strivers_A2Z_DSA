from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        revadj = [[] for _ in range(n)]
        outdeg = [0] * n

        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                revadj[neighbor].append(i)
            outdeg[i] = len(neighbors)

        queue = deque([i for i in range(n) if outdeg[i] == 0])
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            for parent in revadj[node]:
                outdeg[parent] -= 1
                if outdeg[parent] == 0:
                    queue.append(parent)

        return [i for i in range(n) if safe[i]]

# Link: https://leetcode.com/problems/find-eventual-safe-states/
