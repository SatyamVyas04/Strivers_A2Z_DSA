class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


def insertAtTail(head: Node, k: int) -> Node:
    # Write your code here
    if not head:
        head = Node(k)
        return head
    
    temp = head
    while temp and temp.next:
        temp = temp.next
    
    x = Node(k)
    x.prev = temp
    temp.next = x
    return head

# Link: https://www.codingninjas.com/studio/problems/insert-at-end-of-doubly-linked-list_8160464