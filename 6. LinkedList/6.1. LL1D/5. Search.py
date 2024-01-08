'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def searchInLinkedList(head, k):
    # Your code goes here.
    temp = head
    while temp:
        if temp.data == k:
            return 1
        temp = temp.next
    return 0

# Link: https://www.codingninjas.com/studio/problems/search-in-a-linked-list_975381