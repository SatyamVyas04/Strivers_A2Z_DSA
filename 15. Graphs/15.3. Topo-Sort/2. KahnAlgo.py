from collections import deque


class Solution:
    def topologicalSort(self, adj):
        n = len(adj)
        in_degree = [0] * n

        for i in range(n):
            for node in adj[i]:
                in_degree[node] += 1

        queue = deque([i for i in range(n) if in_degree[i] == 0])

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == n else []


# Link: https://www.geeksforgeeks.org/problems/topological-sort/1
