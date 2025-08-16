class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(firstHead, secondHead):
    # Write your code here.
    temp1 = firstHead
    temp2 = secondHead
    val: [Node] = []
    while temp1:
        val.append(temp1)
        temp1 = temp1.next
    while temp2:
        if temp2 in val:
            return temp2
        temp2 = temp2.next
    return None

# Link: https://www.codingninjas.com/studio/problems/-intersection-of-two-linked-lists_630457
