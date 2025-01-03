from typing import List


class Solution:
    def hasCycleDirected(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        color = [0] * v
        for i in range(0, v):
            if color[i] == 0:
                if not self.bfs(graph, i, color):
                    return False
        return True

    def bfs(self, graph, src, color):
        color[src] = 1
        for i in graph[src]:
            if color[i] == 0:
                if not self.bfs(graph, i, color):
                    return False
            elif color[i] == 1:
                return False
        return True

# Simpler version of the last questions, we just need to see if there is a cycle in the graph or not, which can be detected using just 1 color, that is 1 for visited and 0 for not visited.
