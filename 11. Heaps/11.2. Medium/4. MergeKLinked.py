from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        queue = PriorityQueue()
        for idx, l in enumerate(lists):
            if l:
                queue.put((l.val, idx, l))

        dummy = ListNode(0) # type: ignore
        temp = dummy
        while not queue.empty():
            val, idx, node = queue.get()
            temp.next = node
            temp = temp.next
            if queue.empty():
                break
            if node.next:
                queue.put((node.next.val, idx, node.next))

        return dummy.next

# Link: https://leetcode.com/problems/merge-k-sorted-lists/