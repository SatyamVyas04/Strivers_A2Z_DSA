class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def addOne(head: Node) -> Node:
    # write your code here
    carry = carrygen(head)
    if carry:
        return Node(1, head)
    return head


def carrygen(temp):
    if temp == None:
        return 1
    carry = carrygen(temp.next)
    temp.data += carry
    if temp.data == 10:
        temp.data = 0
        return 1
    return 0

# Link: https://www.codingninjas.com/studio/problems/add-one-to-a-number-represented-as-linked-list_920557
