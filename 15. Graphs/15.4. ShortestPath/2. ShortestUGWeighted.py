from collections import defaultdict, deque
from math import inf


class Solution:

    def shortestPath(self, n: int, e: int, edges):
        adj = defaultdict(list)
        for i in range(e):
            u, v, w = edges[i]
            adj[u].append((v, w))

        dist = [inf] * n
        dist[0] = 0
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nei, weight in adj[node]:
                if dist[node] + weight < dist[nei]:
                    dist[nei] = weight + dist[node]
                    queue.append(nei)
        dist = [d if d != inf else -1 for d in dist]
        return dist

# Link: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
