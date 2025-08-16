# class Solution:
#     def countNodes(self, root):
#         """
#         Count the total number of nodes in the Complete Binary Tree.

#         :param root: TreeNode, the root of the binary tree
#         :return: int, total number of nodes in the binary tree
#         """
#         if not root:
#             return 0

#         lh = self.findHeightLeft(root)
#         rh = self.findHeightRight(root)

#         if lh == rh:
#             return (1 << lh) - 1
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)

#     def findHeightLeft(self, node):
#         """
#         Find the height of the left subtree.

#         :param node: TreeNode, the root of the subtree
#         :return: int, height of the left subtree
#         """
#         hght = 0
#         while node:
#             hght += 1
#             node = node.left
#         return hght

#     def findHeightRight(self, node):
#         """
#         Find the height of the right subtree.

#         :param node: TreeNode, the root of the subtree
#         :return: int, height of the right subtree
#         """
#         hght = 0
#         while node:
#             hght += 1
#             node = node.right
#         return hght

from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:  # type: ignore
        self.count = 0

        def helper(root):
            if root:
                self.count += 1
                helper(root.left)
                helper(root.right)
        helper(root)
        return self.count

# Link: https://leetcode.com/problems/count-complete-tree-nodes/
