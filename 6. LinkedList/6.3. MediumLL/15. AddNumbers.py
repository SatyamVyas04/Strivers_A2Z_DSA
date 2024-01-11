class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def addTwoNumbers(l1: Node, l2: Node) -> Node:
    # Write your code here.
    ans = Node(-1)
    n1 = []
    n2 = []

    while l1:
        n1.append(f"{l1.data}")
        l1 = l1.next
    while l2:
        n2.append(f"{l2.data}")
        l2 = l2.next

    n1 = int("".join(n1[::-1]))
    n2 = int("".join(n2[::-1]))
    s = str(n1 + n2)[::-1]
    temp = ans

    for i in s:
        temp.next = Node(int(i))
        temp = temp.next

    return ans.next
        
# Link: https://www.codingninjas.com/studio/problems/add-two-numbers_1170520