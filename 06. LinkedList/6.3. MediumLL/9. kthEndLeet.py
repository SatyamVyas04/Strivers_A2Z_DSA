class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next
        
        while fast:
            if fast.next:
                fast = fast.next
                slow = slow.next
            else:
                break

        slow.next = slow.next.next
        return head
    
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/