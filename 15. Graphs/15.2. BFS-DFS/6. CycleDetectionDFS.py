from typing import List


class Solution:
    # Function to simulate BFS traversal and detect cycle in an undirected graph.
    def helper(self, src: int, adj: List[List[int]], vis: List[bool]) -> bool:
        vis[src] = True
        neigh = [(src, -1)]
        # DFS logic goes here
        while neigh:
            node, parent = neigh.pop()
            for adjacent_node in adj[node]:
                if not vis[adjacent_node]:
                    vis[adjacent_node] = True
                    neigh.append((adjacent_node, node))
                elif adjacent_node != parent:
                    return True
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [False] * V
        for i in range(V):
            if not vis[i] and self.helper(i, adj, vis):
                return True
        return False


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
