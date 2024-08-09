# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        if not head or not head.next or k == 0:
            return head

        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        
        k = k % cnt
        if not k:
            return head

        for _ in range(k):
            temp = head
            while temp.next.next and temp:
                temp = temp.next
            last = temp.next
            temp.next = None
            last.next = head
            head = last
        return head
    
# Link: https://leetcode.com/problems/rotate-list/