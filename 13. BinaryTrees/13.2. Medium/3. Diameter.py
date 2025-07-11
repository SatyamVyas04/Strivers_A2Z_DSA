class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.ans = 0

        def maxheight(node):
            if not node:
                return 0
            else:
                left = maxheight(node.left)
                right = maxheight(node.right)
                self.ans = max(self.ans, left+right)
                return max(left, right) + 1
        maxheight(root)
        return self.ans

# Link: https://leetcode.com/problems/diameter-of-binary-tree/