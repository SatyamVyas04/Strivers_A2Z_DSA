class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getTreeTraversal(root):
    def preorder(node, result):
        if node:
            result.append(node.data)
            preorder(node.left, result)
            preorder(node.right, result)

    def inorder(node, result):
        if node:
            inorder(node.left, result)
            result.append(node.data)
            inorder(node.right, result)

    def postorder(node, result):
        if node:
            postorder(node.left, result)
            postorder(node.right, result)
            result.append(node.data)

    inorder_result = []
    preorder_result = []
    postorder_result = []

    inorder(root, inorder_result)
    preorder(root, preorder_result)
    postorder(root, postorder_result)

    result = (
        " ".join(map(str, inorder_result)) + "\n" +
        " ".join(map(str, preorder_result)) + "\n" +
        " ".join(map(str, postorder_result))
    )

    return result

# Link: https://www.naukri.com/code360/problems/tree-traversal_981269
