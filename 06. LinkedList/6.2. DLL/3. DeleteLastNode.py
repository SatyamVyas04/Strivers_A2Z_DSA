class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def deleteLastNode(head: Node) -> Node | None:
    # Write your code here
    if head.next == None:
        return None

    temp = head

    while temp and temp.next and temp.next.next:
        temp = temp.next

    if temp.next:
        temp.next.prev = None
        temp.next = None
    return head

# Link: https://www.codingninjas.com/studio/problems/delete-last-node-of-a-doubly-linked-list_8160469
