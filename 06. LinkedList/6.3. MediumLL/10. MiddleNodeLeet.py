# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        prev = slow

        if head.next == None:
            return None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = prev.next.next

        return head

# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
