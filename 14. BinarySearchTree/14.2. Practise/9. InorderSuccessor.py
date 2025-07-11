class Solution:
    def inorderSuccessor(self, root, x):
        ans = Node(10000000)  # type: ignore
        while root:
            if x.data >= root.data:
                root = root.right
            else:
                if root.data > x.data and root.data < ans.data:
                    ans = root
                root = root.left
        if ans.data == 10000000:
            ans.data = -1
        return ans

# Link: https://www.geeksforgeeks.org/problems/inorder-successor-in-bst/1