import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_traversals(root):
    preorder = []   # State 1
    inorder = []    # State 2
    postorder = []  # State 3
    stack: list[tuple[TreeNode, int]] = [(root, 1)]

    while stack:
        curr_node, curr_state = stack.pop()
        if curr_state == 1:
            preorder.append(curr_node.val)
            stack.append((curr_node, 2))
            if curr_node.left:
                stack.append((curr_node.left, 1))
        if curr_state == 2:
            inorder.append(curr_node.val)
            stack.append((curr_node, 3))
            if curr_node.right:
                stack.append((curr_node.right, 1))
        if curr_state == 3:
            postorder.append(curr_node.val)

    print(preorder)
    print(inorder)
    print(postorder)


def buildTree(nodes: list) -> TreeNode | None:
    n = len(nodes)
    if n == 0:
        return None
    parentStack = collections.deque()
    root = TreeNode(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = TreeNode(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = TreeNode(nodes[i])
                parentStack.append(curParent.right)
            curParent = parentStack.popleft()
    return root


root = buildTree([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, None, 9, 10])
all_traversals(root=root)

# Link: https://takeuforward.org/data-structure/preorder-inorder-postorder-traversals-in-one-traversal/
