'''
Following is the structure of the Node class already defined:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def segregateEvenOdd(head):
    # Write your code here
    temp = head
    a, b = [], []
    while temp:
        if temp.data % 2:
            a.append(temp.data)
        else:
            b.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        if b:
            temp.data = b.pop(0)
        else:
            temp.data = a.pop(0)
        temp = temp.next
    return head

# Link: https://www.codingninjas.com/studio/problems/segregate-even-and-odd-nodes-in-a-linked-list_1116100
