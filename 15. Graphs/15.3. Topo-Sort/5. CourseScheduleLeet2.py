from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res_stack = []
        queue = deque([])
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            indeg[dst] += 1
            adj[src].append(dst)
        for node, ind in enumerate(indeg):
            if ind == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            res_stack.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    queue.append(nei)

        return res_stack[::-1] if numCourses == len(res_stack) else []

# Link: https://leetcode.com/problems/course-schedule-ii/
