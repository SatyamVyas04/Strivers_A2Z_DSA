from os import *
from sys import *
from collections import *
from math import *

# Linked List Node structure for reference


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(root):
    curr = root
    prev = nex = None
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    return prev


def findkth(root, k):
    for _ in range(k-1):
        if root:
            root = root.next
        else:
            break
    return root


def kReverse(head, k):
    # Write your code here
    # Return the head of the updated linked list.
    temp = head
    prev = None
    nextnode = None
    kthnode = None
    while temp:
        kthnode = findkth(temp, k)
        if not kthnode:
            if prev:
                prev.next = temp
            break
        nextnode = kthnode.next
        kthnode.next = None
        reverse(temp)
        if temp == head:
            head = kthnode
        else:
            prev.next = kthnode

        prev = temp
        temp = nextnode
    return head

# Link: https://www.codingninjas.com/studio/problems/reverse-list-in-k-groups_983644
