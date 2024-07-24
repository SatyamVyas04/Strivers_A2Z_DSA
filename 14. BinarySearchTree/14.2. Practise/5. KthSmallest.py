# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int: # type: ignore
        arr = []
        while root:
            arr.append(root)
            root = root.left
        while k:
            curr = arr.pop()
            k -= 1
            if k == 0:
                return curr.val
            right = curr.right
            while right:
                arr.append(right)
                right = right.left
        return -1

# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/