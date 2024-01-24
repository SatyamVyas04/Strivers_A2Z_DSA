# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: list[TreeNode]) -> int:
        paths = []
        ans = 0

        def dfs(node, currpath):
            if not node:
                return 0

            if node.val in currpath:
                currpath.remove(node.val)
            else:
                currpath.add(node.val)

            if not node.left and not node.right:
                return 1 if len(currpath) <= 1 else 0

            left = dfs(node.left, set(currpath))
            right = dfs(node.right, set(currpath))

            return left + right

        return dfs(root, set())
