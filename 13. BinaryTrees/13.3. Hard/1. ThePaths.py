from typing import Optional, List
from collections import deque


class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        res = []

        def dfs(root, stack):
            if not root:
                return
            # add
            stack.append(root.data)
            # if not left or not right
            if not root.left and not root.right:
                res.append(stack[:])
            # go left
            if root.left:
                dfs(root.left, stack)
            # go right
            if root.right:
                dfs(root.right, stack)
            # remove
            stack.pop()

        dfs(root, [])
        print(res)
        return res


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

# Link: https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1
