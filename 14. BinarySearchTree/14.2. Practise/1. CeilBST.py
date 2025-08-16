class Solution:
    def findCeil(self, root, inp):
        ceil = -1
        while root:
            if root.key == inp:
                ceil = root.key
                return ceil
            if inp > root.key:
                root = root.right
            else:
                ceil = root.key
                root = root.left
        return ceil

# Link: https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
