class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    temp = head
    arr = []
    while temp:
        nex = temp.next
        while temp.child:
            arr.append(temp.data)
            temp = temp.child
        arr.append(temp.data)
        temp = nex
    
    arr.sort()
    dummy = Node(-1)
    t = dummy
    for i in arr:
        t.child = Node(i)
        t = t.child
    return dummy.child
    
# Link: https://www.codingninjas.com/studio/problems/flatten-a-linked-list_1112655