class Solution(object):
    def isValidBST(self, root, lessThan=float('inf'), largerThan=float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
            self.isValidBST(root.right, lessThan, max(root.val, largerThan))

# Link: https://leetcode.com/problems/validate-binary-search-tree/description/
