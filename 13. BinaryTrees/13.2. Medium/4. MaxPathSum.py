# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:  # type: ignore
        maximum = float("-inf")

        def dfs(node):
            nonlocal maximum
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            curr_total = left + node.val + right
            maximum = max(maximum, curr_total)

            return max(0, node.val + max(left, right))

        dfs(root)
        return maximum

# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
