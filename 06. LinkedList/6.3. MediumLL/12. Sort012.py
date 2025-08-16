class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sortList(head):
    # Write your code here
    temp = head
    if not head or not head.next:
        return head

    a = zero = Node(-1)
    b = ones = Node(-1)
    c = twos = Node(-1)

    while temp:
        if temp.data == 0:
            a.next = Node(0)
            a = a.next
        elif temp.data == 1:
            b.next = Node(1)
            b = b.next
        else:
            c.next = Node(2)
            c = c.next
        temp = temp.next

    if zero.next:
        zero = zero.next
    if ones.next:
        ones = ones.next
    if twos.next:
        twos = twos.next

    a.next = ones
    b.next = twos
    return zero

# Link: https://www.codingninjas.com/studio/problems/sort-linked-list-of-0s-1s-2s_1071937
