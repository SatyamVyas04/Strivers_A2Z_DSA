class Solution:
    def floor(self, root, x):
        self.ans = -1
        while root:
            if root.data == x:
                self.ans = root.data
                break
            elif root.data < x:
                self.ans = root.data
                root = root.right
            else:
                root = root.left
        return self.ans

# Link: https://www.geeksforgeeks.org/problems/floor-in-bst/1
