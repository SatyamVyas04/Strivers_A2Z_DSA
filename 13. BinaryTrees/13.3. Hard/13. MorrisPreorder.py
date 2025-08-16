# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root) -> list[int]:
        preorder = []
        curr = root
        while curr:
            if not curr.left:
                preorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    preorder.append(curr.val)
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return preorder

# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
