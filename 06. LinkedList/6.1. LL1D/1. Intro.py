class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def constructLL(arr: [int]) -> Node:
    # Write your code here
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

# Link: https://www.codingninjas.com/studio/problems/introduction-to-linked-list_8144737
