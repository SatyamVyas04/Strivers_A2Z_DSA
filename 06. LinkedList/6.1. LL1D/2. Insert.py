class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def insertAtFirst(l: Node, newValue: int) -> Node:
    # Write your code here
    new = Node(newValue, l)
    return new

# Link: https://www.codingninjas.com/studio/problems/insert-node-at-the-beginning_8144739