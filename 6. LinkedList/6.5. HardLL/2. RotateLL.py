class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next


def rotate(head: Node, k: int) -> Node:
    # Write your code here.
    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.next
    k = k % cnt
    for _ in range(k):
        temp = head
        while temp.next.next and temp:
            temp = temp.next
        last = temp.next
        temp.next = None
        last.next = head
        head = last
    return head

# Link: https://www.codingninjas.com/studio/problems/rotate-linked-list_920454