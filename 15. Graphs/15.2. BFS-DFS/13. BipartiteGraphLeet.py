from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        color = [-1] * v
        for i in range(0, v):
            if color[i] == -1:
                if not self.bfs(graph, i, color, 0):
                    return False
        return True

    def bfs(self, graph, src, color, col):
        color[src] = col
        for i in graph[src]:
            if color[i] == -1:
                if not self.bfs(graph, i, color, 1 - col):
                    return False
            elif color[i] == col:
                return False
        return True

# Link: https://leetcode.com/problems/is-graph-bipartite/submissions/1496558744/
