'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''


def isPalindrome(head):
    # write your code here
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next

    if arr == arr[::-1]:
        return True
    return False

# Link: https://www.codingninjas.com/studio/problems/check-if-linked-list-is-palindrome_985248
