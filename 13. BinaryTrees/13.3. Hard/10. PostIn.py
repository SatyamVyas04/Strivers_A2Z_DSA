class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]: # type: ignore
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])  # type: ignore
        idx = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        return root

# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/