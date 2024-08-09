'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def reverseLinkedList(head):
    # write your code here
    if not head.next:
        return head
    
    curr = head
    prev = next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Link: https://www.codingninjas.com/studio/problems/reverse-linked-list_920513