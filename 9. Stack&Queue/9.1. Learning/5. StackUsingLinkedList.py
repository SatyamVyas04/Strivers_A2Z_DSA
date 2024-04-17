class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Stack:
    # Write your code here
    def __init__(self):
        # Write your code here
        self.root = Node(-1)

    def getSize(self):
        # Write your code here
        temp = self.root
        count = -1
        while temp:
            count += 1
            temp = temp.next
        return count

    def isEmpty(self):
        # Write your code here
        if self.getSize() == 0:
            return True
        return False

    def push(self, data):
        # Write your code here
        temp = self.root
        if self.isEmpty():
            self.root.next = Node(data)
        else:
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        return

    def pop(self):
        # Write your code here
        temp = self.root
        if self.isEmpty():
            return -1
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        if prev:
            prev.next = None

    def getTop(self):
        # Write your code here
        temp = self.root
        if self.isEmpty():
            return -1
        while temp.next:
            temp = temp.next
        return temp.data

# Link: https://naukri.com/code360/problems/implement-stack-with-linked-list_1279905