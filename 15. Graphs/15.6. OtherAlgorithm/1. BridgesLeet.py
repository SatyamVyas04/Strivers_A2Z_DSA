# Tarjan's Bridge Finding Algorithm

class Solution:
    def criticalConnections(self, n: int, connections):
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []

        def dfs(node, parent, timer):
            vis[node] = 1
            tin[node] = low[node] = timer
            timer += 1
            for nei in adj[node]:
                if nei == parent:
                    continue
                if vis[nei] == 0:
                    dfs(nei, node, timer)
                    low[node] = min(low[node], low[nei])
                    if low[nei] > tin[node]:
                        bridges.append((node, nei))
                else:
                    low[node] = min(low[node], low[nei])

        dfs(0, -1, 0)
        return bridges

# Link: https://leetcode.com/problems/critical-connections-in-a-network/submissions/1504368957/
