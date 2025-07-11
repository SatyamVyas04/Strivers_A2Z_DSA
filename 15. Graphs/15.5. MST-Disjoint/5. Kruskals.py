import heapq


class UnionFind:
    def __init__(self, n):
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
        self.parent = [i for i in range(n+1)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
        if self.size[parent_u] < self.size[parent_v]:
            self.parent[parent_u] = parent_v
            self.size[parent_v] += self.size[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]

    def union_by_rank(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
        if self.rank[parent_u] < self.rank[parent_v]:
            self.parent[parent_u] = parent_v
        elif self.rank[parent_v] < self.rank[parent_u]:
            self.parent[parent_v] = parent_u
        else:
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1


class Solution:
    def spanningTree(self, V, adj):
        unionfind = UnionFind(V)
        minheap = []  # (w, u, v)
        visited_edges = set()
        for u in range(V):
            for v, w in adj[u]:
                if (u, v) not in visited_edges and (v, u) not in visited_edges:
                    heapq.heappush(minheap, (w, u, v))
                    visited_edges.add((u, v))

        weight = 0
        edges_used = 0
        while minheap and edges_used < V - 1:
            w, u, v = heapq.heappop(minheap)
            if unionfind.find(u) != unionfind.find(v):
                unionfind.union_by_rank(u, v)
                weight += w
                edges_used += 1

        return weight

# Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
