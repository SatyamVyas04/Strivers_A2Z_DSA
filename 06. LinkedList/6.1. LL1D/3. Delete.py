class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteLast(head: Node) -> Node:
    # Write your code here
    temp = head
    while temp.next.next!=None:
        temp = temp.next
    temp.next = None
    return head

# Link: https://www.codingninjas.com/studio/problems/delete-node-of-linked-list_8160463