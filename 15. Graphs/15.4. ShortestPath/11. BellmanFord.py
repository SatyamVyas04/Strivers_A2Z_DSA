class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [100_000_000] * V
        dist[src] = 0
        for _ in range(V):
            for u, v, w in edges:
                if dist[u] != 100_000_000 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in edges:
            if dist[u] != 100_000_000 and dist[u] + w < dist[v]:
                return [-1]
        return dist

# Link: https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
