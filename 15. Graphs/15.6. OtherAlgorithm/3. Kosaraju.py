class Solution:
    def kosaraju(self, adj):
        n = len(adj)
        vis = [0] * n
        stack = []

        def dfs(node, adj):
            vis[node] = 1
            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei, adj)
            stack.append(node)

        for i in range(n):
            if not vis[i]:
                dfs(i, adj)

        revadj = [[] for _ in range(n)]
        for i in range(n):
            vis[i] = 0
            for nei in adj[i]:
                revadj[nei].append(i)

        scc = 0
        while stack:
            node = stack.pop()
            if not vis[node]:
                dfs(node, revadj)
                scc += 1

        return scc

# Link: https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1
