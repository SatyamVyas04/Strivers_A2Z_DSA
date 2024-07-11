class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: # type: ignore
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0]) # type: ignore
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/