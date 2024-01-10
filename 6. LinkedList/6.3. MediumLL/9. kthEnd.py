'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    # Write your code here.
    slow = fast = head
    for i in range(k):
        fast = fast.next

    if fast == None:
        return head.next
    
    while fast:
        if fast.next:
            fast = fast.next
            slow = slow.next
        else:
            break

    slow.next = slow.next.next
    return head

# Link: https://www.codingninjas.com/studio/problems/delete-kth-node-from-end_799912