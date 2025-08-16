from typing import Optional


class Solution:
    # type: ignore
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(root, val):
            if not root:
                return TreeNode(val)  # type: ignore

            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)  # type: ignore
                else:
                    root.left = helper(root.left, val)

            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)  # type: ignore # type: ignore
                else:
                    root.right = helper(root.right, val)

            return root

        return helper(root, val)

# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
