class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head: Node, k: int) -> Node:
    # Write your code here
    while head.next and head.data == k:
        head.next.prev = None
        head = head.next
    if head.data == k:
        return None

    temp = head
    while temp and temp.next:
        if temp.next.data == k:
            temp.next = temp.next.next
            if temp.next:
                temp.next.prev = temp
        temp = temp.next
    return head

# Link: https://www.codingninjas.com/studio/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461
