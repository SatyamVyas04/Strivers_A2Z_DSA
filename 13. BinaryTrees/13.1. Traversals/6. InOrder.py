# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]: #type: ignore
        self.ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.ans

# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/