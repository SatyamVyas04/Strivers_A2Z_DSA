class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: None | TreeNode = None
        self.right: None | TreeNode = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode | None, p: 'TreeNode', q: 'TreeNode') -> TreeNode | None:
        p, q = sorted([p.val, q.val])
        while root != None:
            if p < root.val and q > root.val:
                return root
            elif p == root.val or q == root.val:
                return root
            elif p > root.val and q > root.val:
                root = root.right
            else:
                root = root.left

# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/1331856673/
