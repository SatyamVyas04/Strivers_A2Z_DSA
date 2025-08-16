'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def deleteMiddle(head):
    # Write your code here.
    slow = fast = head
    prev = slow

    if head.next == None:
        return None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = prev.next.next

    return head

# Link: https://www.codingninjas.com/studio/problems/delete-middle-node_763267
