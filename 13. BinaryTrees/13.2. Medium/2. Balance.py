class Solution:
    def isBalanced(self, root):
        self.Bal = True

        def dfs(node):
            if not node:
                return 0

            left_sub_height, right_sub_height = dfs(node.left), dfs(node.right)

            if abs(left_sub_height - right_sub_height) > 1:
                self.Bal = False

            return max(left_sub_height, right_sub_height) + 1

        dfs(root)
        return self.Bal

# Link: https://leetcode.com/problems/balanced-binary-tree/
