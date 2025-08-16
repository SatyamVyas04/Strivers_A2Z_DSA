class Solution:
    def distanceK(self, root, target, k: int):
        if not root:
            return []

        hashmap = {}

        def setparents(node, parent=None):
            if node:
                hashmap[node] = parent
                setparents(node.left, node)
                setparents(node.right, node)

        setparents(root)

        distance = 0
        q = [target]
        vis = set()

        while q:
            if distance == k:
                return [node.val for node in q]

            next_q = []
            for curr in q:
                vis.add(curr)
                parent = hashmap[curr]
                if parent and parent not in vis:
                    next_q.append(parent)
                if curr.left and curr.left not in vis:
                    next_q.append(curr.left)
                if curr.right and curr.right not in vis:
                    next_q.append(curr.right)

            q = next_q
            distance += 1

        return []

# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/1314157760/
