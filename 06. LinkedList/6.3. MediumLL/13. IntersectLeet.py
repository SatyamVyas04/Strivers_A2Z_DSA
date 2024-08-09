# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:  
        n1, n2 = 0, 0
        a = headA
        b = headB
        while a:
            n1 += 1
            a = a.next
        while b:
            n2 += 1
            b = b.next
        
        a = headA
        b = headB
        if n1 < n2:
            for i in range(n2-n1):
                b = b.next
        else:
            for j in range(n1-n2):
                a = a.next

        while a and b:
            if a == b:
                return a
            else:
                a = a.next
                b = b.next
        return None
    
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/