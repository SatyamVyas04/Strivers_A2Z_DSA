# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        met = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                met = True
                break
        if not met:
            return None
        else:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
        return slow

# Link: https://leetcode.com/problems/linked-list-cycle-ii/
