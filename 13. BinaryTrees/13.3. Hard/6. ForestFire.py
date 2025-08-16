class Solution:
    def minTime(self, root, target):
        return self.distanceK(root, target)

    def distanceK(self, root, target):
        if not root:
            return []

        hashmap = {}

        def setparents(node, parent=None):
            nonlocal target
            if node:
                hashmap[node.data] = parent
                setparents(node.left, node)
                setparents(node.right, node)
                if node.data == target:
                    target = node

        setparents(root)

        distance = 0
        q = [target]
        vis = set()

        while q:
            next_q = []
            for curr in q:
                vis.add(curr)
                parent = hashmap[curr.data]
                if parent and parent not in vis:
                    next_q.append(parent)
                if curr.left and curr.left not in vis:
                    next_q.append(curr.left)
                if curr.right and curr.right not in vis:
                    next_q.append(curr.right)

            q = next_q
            distance += 1

        return distance

# Link: https://www.geeksforgeeks.org/problems/burning-tree/1
