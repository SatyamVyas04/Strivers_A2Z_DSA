from collections import defaultdict


class Solution:
    def numProvinces(self, adj, V):
        isConnected = adj
        n = V
        edges = defaultdict(list)

        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1 and row != col:
                    edges[row].append(col)
                    edges[col].append(row)

        visited = set()
        count = 0

        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    for nei in edges[curr]:
                        stack.append(nei)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count

# Link: https://www.geeksforgeeks.org/problems/number-of-provinces/1
