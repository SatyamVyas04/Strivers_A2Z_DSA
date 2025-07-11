class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return []
        width, level = 0, [(root, 1)]
        # Keep going untill current level has some nodes.
        while len(level):
            # Put all children of current level in next_level.
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:   # Make sure to not put the Null nodes
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2+1))
            level = next_level
        return width

# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/1314024222/