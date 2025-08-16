class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:  # type: ignore
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root, 0)

# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
