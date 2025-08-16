class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        if not root.left:
            return root.data
        else:
            return self.minValue(root.left)

# Link: https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1
