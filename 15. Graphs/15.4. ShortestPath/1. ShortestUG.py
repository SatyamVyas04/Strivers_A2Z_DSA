from collections import deque
from math import inf


class Solution:
    def shortestPath(self, adj, src):
        n = len(adj)
        dist = [inf] * n
        dist[src] = 0
        queue = deque([src])
        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                if dist[node] + 1 < dist[nei]:
                    dist[nei] = 1 + dist[node]
                    queue.append(nei)
        dist = [d if d != inf else -1 for d in dist]
        return dist

# Link: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
