class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: list[int]) -> Node:
    # Write your code here
    head = Node(0)
    temp = head
    for i in arr:
        newnode = Node(i)
        temp.next = newnode
        newnode.prev = temp
        temp = temp.next
    return head.next

# Link: https://www.codingninjas.com/studio/problems/introduction-to-doubly-linked-list_8160413
