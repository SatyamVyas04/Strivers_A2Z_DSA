from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        return numCourses == len(res_stack)

# Link: https://leetcode.com/problems/course-schedule/submissions/1498288054/
