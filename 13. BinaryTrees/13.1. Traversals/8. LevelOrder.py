from collections import deque
from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        curr_arr = []
        finalarr = []
        curr_level = 0

        while q:
            curr, l = q.popleft()
            if l > curr_level:
                finalarr.append(curr_arr)
                curr_arr = []
                curr_level = l

            curr_arr.append(curr.val)
            if curr.left:
                q.append((curr.left, l + 1))  # type: ignore
            if curr.right:
                q.append((curr.right, l + 1))  # type: ignore

        if curr_arr:
            finalarr.append(curr_arr)

        return finalarr

# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/1300965130/
