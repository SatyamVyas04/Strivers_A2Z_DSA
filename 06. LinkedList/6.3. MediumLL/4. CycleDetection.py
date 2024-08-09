'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False

# Link: https://www.codingninjas.com/studio/problems/cycle-detection-in-a-singly-linked-list_628974