# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        temp = head
        evenstart = head.next
        fwd = None
        cnt = 0
        while temp.next.next:
            cnt += 1
            fwd = temp.next
            temp.next = temp.next.next
            temp = fwd
        if cnt % 2 == 0:
            # temp == last odd
            # temp.next == last even
            # [7]->[8]->None
            temp.next = evenstart
        else:
            # temp == last even
            # temp.next == last odd
            # [8]->[9]->None
            temp.next.next = evenstart
            temp.next = None
        return head

# Link: https://leetcode.com/problems/odd-even-linked-list/
