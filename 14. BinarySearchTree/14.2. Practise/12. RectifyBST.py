from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = TreeNode(-int(10e9))

        def inorder(root):
            if root:
                inorder(root.left)
                # Logic
                if self.first == None and self.prev.val >= root.val:
                    self.first = self.prev
                if self.first != None and self.prev.val >= root.val:
                    self.second = root
                self.prev = root
                # End of Logic
                inorder(root.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val  # type: ignore

# Link: https://leetcode.com/problems/recover-binary-search-tree/
