from collections import defaultdict


class Solution:
    # type: ignore
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)

        def dfs(node, col, row):
            if not node:
                return
            hashmap[col].append((row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        ans = []
        for col in sorted(hashmap.keys()):
            ans.append([i[-1] for i in sorted(hashmap[col])])
        return ans

# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
