class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def removeDuplicates(head: Node) -> Node:
    # Write your code here
    curr = head
    while curr!=None and curr.next !=None:
        if curr.next.data == curr.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# Link: https://www.codingninjas.com/studio/problems/remove-duplicates-from-a-sorted-doubly-linked-list_2420283