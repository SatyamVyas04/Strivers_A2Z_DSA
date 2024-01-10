class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


def lengthOfLoop(head: Node) -> int:
    # Write your code here
    slow = fast = head
    flag = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            flag = True
            break
    
    if flag:
        cnt = 1
        slow = slow.next
        while slow!=fast:
            cnt += 1
            slow = slow.next
        return cnt
    else:
        return 0

# Link: https://www.codingninjas.com/studio/problems/find-length-of-loop_8160455