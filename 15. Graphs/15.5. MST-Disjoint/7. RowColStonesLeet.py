class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0


class Solution:
    def removeStones(self, stones) -> int:
        uf = UnionFind()

        for r, c in stones:
            uf.add(r)
            uf.add(c + 100000)  # Offset to differentiate row and column
            uf.union(r, c + 100000)

        root_set = set()
        for r, c in stones:
            root_set.add(uf.find(r))

        # Maximum stones that can be removed
        return len(stones) - len(root_set)

# Haha had done this earlier, probably in DCC
# Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
