# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        cur = None
        nex = None
        while length >= k:
            cur = pre.next
            nex = cur.next
            for i in range(1, k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            length -= k
        return dummyHead.next
    
# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/