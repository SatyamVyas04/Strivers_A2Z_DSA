'''
	Time Complexity : O(N ^ 2)
	Space Complexity : O(N)

	Where N is the size of the stack.
'''


def sortedInsert(stack, key):

    if (len(stack) == 0 or key > stack[-1]):

        stack.append(key)
        return

    top = stack[-1]
    stack.pop()

    # Recur for the remaining elements in the stack.
    sortedInsert(stack, key)

    # Insert the popped element back into the stack.
    stack.append(top)


def sortStackHelper(s):

    if (len(s) == 0):
        return

    top = s[-1]
    s.pop()

    # Recur for the remaining elements in the stack.
    sortStackHelper(s)

    # Insert the popped element back into the sorted S.
    sortedInsert(s, top)


def sortStack(s):

    sortStackHelper(s)
    return s

# Link: https://www.codingninjas.com/studio/problems/sort-stack_1229505
