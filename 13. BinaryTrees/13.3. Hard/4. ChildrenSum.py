class Solution:
    def isSumProperty(self, root):
        if not root or (not root.left and not root.right):
            return 1
        else:
            total = 0
            if root.left:
                total += root.left.data
            if root.right:
                total += root.right.data
            return int(root.data == total and self.isSumProperty(root.left) and self.isSumProperty(root.right))

# Link: https://www.geeksforgeeks.org/problems/children-sum-parent/1
