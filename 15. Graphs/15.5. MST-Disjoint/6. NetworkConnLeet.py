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
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        unionfind = UnionFind(n)
        for u, v in connections:
            unionfind.union_by_size(u, v)

        connected_components = len(set(unionfind.find(i) for i in range(n)))

        return connected_components - 1

# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/submissions/1503336290/
