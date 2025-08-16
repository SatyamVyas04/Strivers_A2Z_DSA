# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = carry = 0
        temp1 = l1
        temp2 = l2
        n1, n2 = 0, 0
        while temp1:
            n1 += 1
            temp1 = temp1.next
        while temp2:
            n2 += 1
            temp2 = temp2.next
        # Larger of two LLs in LL1
        if n2 > n1:
            n1, n2 = n2, n1
            l1, l2 = l2, l1

        a = l1
        b = l2
        prev = None
        while b:
            prev = a
            carry, digit = divmod(a.val + b.val + carry, 10)
            a.val = digit
            a = a.next
            b = b.next

        if n1 != n2:
            while a:
                prev = a
                carry, digit = divmod(a.val + carry, 10)
                a.val = digit
                a = a.next

        if carry == 1:
            prev.next = ListNode(1)
            return l1
        return l1

# Link: https://leetcode.com/problems/add-two-numbers/
