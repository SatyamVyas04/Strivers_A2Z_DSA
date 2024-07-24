from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        inorder = []
        curr = root
        while curr:
            if not curr.left:
                inorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                if prev.right == curr:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right

        self.inorder = inorder
        self.ptr = 0
        self.cap = len(inorder)

    def next(self):
        if self.ptr >= self.cap:
            return None
        else:
            self.ptr += 1
            return self.inorder[self.ptr - 1]

    def hasNext(self) -> bool:
        if self.ptr < self.cap:
            return True
        return False

# Link: https://leetcode.com/problems/binary-search-tree-iterator/
