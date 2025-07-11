import heapq


class Solution:
    def spanningTree(self, V, adj):
        vis = set()
        min_heap = [(0, 0)]
        total_weight = 0

        while len(vis) < V:
            weight, u = heapq.heappop(min_heap)
            if u in vis:
                continue
            vis.add(u)
            total_weight += weight

            for v, w in adj[u]:
                if v not in vis:
                    heapq.heappush(min_heap, (w, v))

        return total_weight

# Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
