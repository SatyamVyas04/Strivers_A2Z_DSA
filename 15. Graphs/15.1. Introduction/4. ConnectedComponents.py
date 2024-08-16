from typing import List


class Solution:  # more literal
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize parent array for union-find
        parent = [i for i in range(n)]

        # Perform union-find on each edge
        for u, v in edges:
            self.union(u, v, parent)

        # Count the number of distinct parents (connected components)
        count = len(set(self.find(x, parent) for x in range(n)))
        return count

    def union(self, x: int, y: int, parent: List[int]) -> None:
        rootX = self.find(x, parent)
        rootY = self.find(y, parent)
        if rootX != rootY:
            parent[rootX] = rootY

    def find(self, x: int, parent: List[int]) -> int:
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

# Link: https://leetcode.ca/2016-10-18-323-Number-of-Connected-Components-in-an-Undirected-Graph/
