from collections import deque
from sys import maxsize
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Create a queue for nodes that need to be visited and add the root
        queue = deque()
        current = root
        queue.append(current)

        # Keeps track of whether we are on an even level
        even = True

        # While there are more nodes in the queue
        # Determine the size of the level and handle the nodes
        while queue:
            size = len(queue)

            # Prev holds the value of the previous node in this level
            prev = maxsize
            if even:
                prev = -maxsize

            # While there are more nodes in this level
            # Remove a node, check whether it satisfies the conditions
            # Add its children to the queue
            while size > 0:
                current = queue.popleft()

                # If on an even level, check that the node's value is odd and greater than prev
                # If on an odd level, check that the node's value is even and less than prev
                if (even and (current.val % 2 == 0 or current.val <= prev)) or \
                        (not even and (current.val % 2 == 1 or current.val >= prev)):
                    return False

                prev = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                # Decrement size, we have handled a node on this level
                size -= 1

            # Flip the value of even, the next level will be opposite
            even = not even

        # If every node meets the conditions, the tree is Even-Odd
        return True
