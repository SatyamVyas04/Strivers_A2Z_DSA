'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''


def reverseDLL(head):
    # Write your code here
    curr = head
    prev, next = None, None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Link: https://www.codingninjas.com/studio/problems/reverse-a-doubly-linked-list_1116098
