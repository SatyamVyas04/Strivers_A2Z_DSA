import sys
sys.setrecursionlimit(10**6)


class Solution:
    def articulationPoints(self, n, adj):
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        ans = set()

        def dfs(node, parent, timer):
            child = 0
            vis[node] = 1
            tin[node] = low[node] = timer
            timer += 1
            for nei in adj[node]:
                if nei == parent:
                    continue
                if vis[nei] == 0:
                    child += 1
                    dfs(nei, node, timer)
                    low[node] = min(low[node], low[nei])
                    if low[nei] >= tin[node] and parent != -1:
                        ans.add(node)
                else:
                    low[node] = min(low[node], tin[nei])
            if child > 1 and parent == -1:
                ans.add(node)

        dfs(0, -1, 0)
        return sorted(list(ans)) if ans else [-1]

# Link: https://www.geeksforgeeks.org/problems/articulation-point-1/1
