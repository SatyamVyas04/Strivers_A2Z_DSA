from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        if not root:
            return []

        q = deque([(root, 0)])
        curr_arr = []
        finalarr = []
        curr_level = 0

        while q:
            curr, l = q.popleft()
            if l > curr_level:
                finalarr.append(curr_arr)
                curr_arr = []
                curr_level = l

            curr_arr.append(curr.val)
            if curr.left:
                q.append((curr.left, l + 1))  # type: ignore
            if curr.right:
                q.append((curr.right, l + 1))  # type: ignore

        if curr_arr:
            finalarr.append(curr_arr)

        # Modification
        for i in range(len(finalarr)):
            finalarr[i] = finalarr[i][-1]
        return finalarr
