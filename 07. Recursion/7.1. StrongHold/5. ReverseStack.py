"""
    Time Complexity: O(N^2)
    Space Complexity: O(N)

    where 'N' is the total number of elements in the given stack.
"""

from typing import List


def insertAtBottom(stack: List[int], ele: int) -> None:
    """
    Recursive function to insert an element at the bottom of the stack.
    """
    if not stack:
        # If the stack is empty, simply push the element.
        stack.append(ele)
        return

    # If the stack is not empty, remove the top element.
    top = stack.pop()

    # Recursively call insertAtBottom to insert the element at the bottom.
    insertAtBottom(stack, ele)

    # Push the removed top element back onto the stack.
    stack.append(top)


def reverseStack(stack: List[int]) -> None:
    """
    Function to reverse the elements of the stack.
    """
    if not stack:
        # Base case: If the stack is empty, no elements to reverse.
        return

    # If the stack is not empty, remove the top element.
    top = stack.pop()

    # Recursively call reverseStack to reverse the remaining elements.
    reverseStack(stack)

    # After reversing the remaining elements, insert the removed top element at the bottom.
    insertAtBottom(stack, top)

# Link: https://www.codingninjas.com/studio/problems/reverse-stack-using-recursion_631875
