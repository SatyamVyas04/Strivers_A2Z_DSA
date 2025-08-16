# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:  # type: ignore
        if not root:
            return

        if root.left and root.right:
            temp = root.left
            while temp.right:
                temp = temp.right
            temp.right = root.right
            root.right = root.left

        elif root.left:
            root.right = root.left

        root.left = None
        self.flatten(root.right)
        return root

# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
