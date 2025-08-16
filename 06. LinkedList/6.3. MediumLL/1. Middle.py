from math import *
from collections import *
from sys import *
from os import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''


def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Link: https://www.codingninjas.com/studio/problems/middle-of-linked-list_973250
