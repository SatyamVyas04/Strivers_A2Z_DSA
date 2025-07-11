class Solution:
    def topologicalSort(self, adj):
        nodes = len(adj)
        visited = [0] * nodes
        result_stack = []

        def dfs(node):
            if visited[node]:
                return
            visited[node] = 1
            for nei in adj[node]:
                dfs(nei)
            result_stack.append(node)

        for node in range(nodes):
            if not visited[node]:
                dfs(node)

        return result_stack[::-1]

# Link: https://www.geeksforgeeks.org/problems/topological-sort/1
