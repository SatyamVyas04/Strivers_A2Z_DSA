class Node:
    def __init__(self, data=0, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


def cloneLL(head: Node) -> Node:
    # Write your code here
    if not head:
        return None
    
    curr = head
    while curr:
        new_node = Node(curr.data, curr.next)
        curr.next = new_node
        curr = new_node.next
        
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    old_head = head
    new_head = head.next
    curr_old = old_head
    curr_new = new_head
    
    while curr_old:
        curr_old.next = curr_old.next.next
        curr_new.next = curr_new.next.next if curr_new.next else None
        curr_old = curr_old.next
        curr_new = curr_new.next
        
    return new_head

# Link: https://www.codingninjas.com/studio/problems/clone-a-linked-list-with-random-pointers_983604