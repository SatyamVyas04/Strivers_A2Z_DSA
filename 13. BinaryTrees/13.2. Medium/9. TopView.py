from collections import defaultdict


class Solution:
    def topView(self, root):
        hashmap = defaultdict(list)
        counter = [0]

        def dfs(node, col, row):
            if not node:
                return
            hashmap[col].append((row, counter[0], node.data))
            counter[0] += 1
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        ans = []
        for col in sorted(hashmap.keys()):
            col_nodes = sorted(hashmap[col], key=lambda x: (x[0], x[1]))
            ans.append(col_nodes[0][2])
        return ans

# Link: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
