# Functions to traverse on each part.
def traverseBoundary(root):
    def isLeaf(root):
        return not root.left and not root.right

    def addLeftBoundary(root, res):
        curr = root.left
        while curr:
            if not isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addRightBoundary(root, res):
        curr = root.right
        temp = []
        while curr:
            if not isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        for i in range(len(temp) - 1, -1, -1):
            res.append(temp[i])

    def addLeaves(root, res):
        if isLeaf(root):
            res.append(root.data)
            return
        if root.left:
            addLeaves(root.left, res)
        if root.right:
            addLeaves(root.right, res)

    def printBoundary(root):
        res = []
        if not root:
            return res
        if not isLeaf(root):
            res.append(root.data)

        addLeftBoundary(root, res)
        addLeaves(root, res)
        addRightBoundary(root, res)

        return res

    return printBoundary(root)

# Link: https://www.naukri.com/code360/problems/boundary-traversal_790725?leftPanelTabValue=PROBLEM
