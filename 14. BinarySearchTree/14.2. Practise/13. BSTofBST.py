class NodeVal:
    def __init__(self, minNode, maxNode, maxSize) -> None:
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize


class Solution:
    def largestBst(self, root):
        return self.helper(root).maxSize

    def helper(self, root):
        if not root:
            return NodeVal(10e9, -10e9, 0)

        left: NodeVal = self.helper(root.left)
        right: NodeVal = self.helper(root.right)
        if left.maxNode < root.data < root.minNode:
            return NodeVal(min(root.data, left.minNode), max(root.data, right.maxNode), 1 + left.maxSize + right.maxSize)

        return NodeVal(-10e9, 10e9, max(left.maxSize, right.maxSize))

# Link: https://www.geeksforgeeks.org/problems/largest-bst/1
