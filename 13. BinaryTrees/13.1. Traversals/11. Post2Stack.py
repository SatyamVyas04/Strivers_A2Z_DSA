# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # type: ignore
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []

        while stack1:
            curr = stack1.pop()
            if not curr:
                continue
            stack1.append(curr.left)
            stack1.append(curr.right)
            stack2.append(curr.val)

        return stack2[::-1]

# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
