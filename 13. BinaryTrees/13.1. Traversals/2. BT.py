class Solution:
    def createTree(self, root, l):
        n = len(l)

        def dfs(root, idx):
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n:
                root.left = Node(l[left])
                dfs(root.left, left)
            if right < n:
                root.right = Node(l[right])
                dfs(root.right, right)

        temp = root
        dfs(temp, 0)


class Node:
    def __init__(self, val):
        self.right: Node | None = None
        self.data = val
        self.left: Node | None = None


def traverseInorder(temp, inorder):
    if (temp != None):
        traverseInorder(temp.left, inorder)
        inorder.append(temp.data)
        traverseInorder(temp.right, inorder)
    return


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        arr = list(map(int, input().split()))
        root = Node(arr[0])
        root.left = Node(arr[1])
        root.right = Node(arr[2])
        root.left.left = Node(arr[3])
        root.left.right = Node(arr[4])
        root.right.left = Node(arr[5])
        root.right.right = Node(arr[6])

        obj = Solution()
        root0 = Node(arr[0])
        obj.createTree(root0, arr)

        a = []
        traverseInorder(root0, a)
        b = []
        traverseInorder(root, b)

        print(a)
        print(b)

        if (a == b):
            print(1)
        else:
            print(-1)
