# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr: TreeNode | None = root
        temp: TreeNode | None = None
        stack: List[TreeNode] = []
        result_arr: List[int] = []
        while curr != None or len(stack):
            if curr != None:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if temp == None:
                    temp = stack[-1]
                    stack.pop()
                    result_arr.append(temp.val)
                    while len(stack) and temp == stack[-1].right:
                        temp = stack[-1]
                        stack.pop()
                        result_arr.append(temp.val)
                else:
                    curr = temp
        return result_arr

# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
