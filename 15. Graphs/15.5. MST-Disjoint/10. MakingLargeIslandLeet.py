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
    def largestIsland(self, grid) -> int:
        ans = 0
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
                for i in range(4):
                    nr, nc = row + dr[i], col + dc[i]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        uf.union_by_size(row * cols + col, nr * cols + nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    continue
                dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
                temp = set()
                for i in range(4):
                    nr, nc = row + dr[i], col + dc[i]
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        temp.add(uf.find(nr * cols + nc))

                ans = max(ans, sum(uf.size[uf.find(node)]
                          for node in temp) + 1)

        for cell in range(rows * cols):
            ans = max(ans, uf.size[uf.find(cell)])

        return ans


# Link: https://leetcode.com/problems/making-a-large-island/
