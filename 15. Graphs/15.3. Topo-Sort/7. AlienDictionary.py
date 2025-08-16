class Solution:
    def findOrder(self, dict, k):
        n = len(dict)
        graph = {chr(i + 97): [] for i in range(k)}

        for i in range(n - 1):
            for j in range(min(len(dict[i]), len(dict[i + 1]))):
                if dict[i][j] != dict[i + 1][j]:
                    graph[dict[i][j]].append(dict[i + 1][j])
                    break
        stack = []
        visited = set()

        def dfs(c):
            if c in visited:
                return
            visited.add(c)
            for adj in graph[c]:
                dfs(adj)
            stack.append(c)

        for c in graph:
            dfs(c)

        stack.reverse()
        order = "".join(stack)
        return order

# Link: https://www.geeksforgeeks.org/problems/alien-dictionary/1
