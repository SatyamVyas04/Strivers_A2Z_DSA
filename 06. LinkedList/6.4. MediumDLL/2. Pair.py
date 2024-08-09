class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def findPairs(head: Node, k: int) -> [[int]]:
    # Write your code here.
    # Return boolean true or false.
    prev = set()
    ans = []
    temp = head
    while temp:
        if k - temp.data in prev:
            ans.append([temp.data, k-temp.data])
        else:
            prev.add(temp.data)
        temp = temp.next
    return ans
    
# Link: https://www.codingninjas.com/studio/problems/find-pairs-with-given-sum-in-doubly-linked-list_1164172