'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def firstNode(head):
    # Write your code here
    slow = fast = head
    flag = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            flag = True
            break
    
    if flag:
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow

    else:
        return None
    
# Link: https://www.codingninjas.com/studio/problems/linked-list-cycle-ii_1112628