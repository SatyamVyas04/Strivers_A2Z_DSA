# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    # type: ignore
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        curr_arr = []
        finalarr = []
        curr_level = 0
        booleanFlag = True

        while q:
            curr, l = q.popleft()
            if l > curr_level and booleanFlag:
                finalarr.append(curr_arr)
                curr_arr = []
                curr_level = l
                booleanFlag = False
            elif l > curr_level and not booleanFlag:
                finalarr.append(curr_arr[::-1])
                curr_arr = []
                curr_level = l
                booleanFlag = True

            curr_arr.append(curr.val)
            if curr.left:
                q.append((curr.left, l + 1))  # type: ignore
            if curr.right:
                q.append((curr.right, l + 1))  # type: ignore

        if curr_arr and booleanFlag:
            finalarr.append(curr_arr)
            booleanFlag = False
        elif curr_arr and not booleanFlag:
            finalarr.append(curr_arr[::-1])
            booleanFlag = True

        return finalarr

# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
