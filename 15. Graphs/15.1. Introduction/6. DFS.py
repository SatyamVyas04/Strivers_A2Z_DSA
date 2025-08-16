class Solution:
    def dfsOfGraph(self, V, adj):
        stack = [0]
        visited = set()
        ans = []

        while stack:
            current = stack.pop()
            if current in visited:
                continue

            ans.append(current)
            visited.add(current)
            subarr = []
            for nei in adj[current]:
                if nei not in visited:
                    subarr.append(nei)

            stack = stack[:] + subarr[::-1]

        return ans

# Link: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
