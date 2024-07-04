# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(-1)
        temp = dummy
        curr = head
        currsum = 0

        while curr:
            if curr.val == 0:
                temp.next = ListNode(currsum)
                temp = temp.next
                currsum = 0
            else:
                currsum += curr.val
            curr = curr.next

        return dummy.next