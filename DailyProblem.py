# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []
        dummy = TreeNode(-1)
        temp = dummy

        def dfs(root, temp):
            if root:
                if root.right:
                    temp.right = TreeNode()
                    dfs(root.right, temp.right)
                nodes.append(root.val)
                temp.val = sum(nodes)
                if root.left:
                    temp.left = TreeNode()
                    dfs(root.left, temp.left)

        dfs(root, temp)
        return dummy

# Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
