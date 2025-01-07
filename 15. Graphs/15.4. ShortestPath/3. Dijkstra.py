from collections import deque
from math import inf


class Solution:
    def dijkstra(self, adj, src):
        dist = [inf] * len(adj)
        dist[src] = 0
        queue = deque([src])
        while queue:
            node = queue.popleft()
            for nei, weight in adj[node]:
                if dist[node] + weight < dist[nei]:
                    dist[nei] = weight + dist[node]
                    queue.append(nei)
        dist = [d if d != inf else -1 for d in dist]
        return dist

# Link: https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
