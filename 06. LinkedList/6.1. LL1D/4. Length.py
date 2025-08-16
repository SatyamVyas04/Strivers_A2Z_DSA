'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''


def length(head):
    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.next
    return cnt

# Link: https://www.codingninjas.com/studio/problems/count-nodes-of-linked-list_5884
