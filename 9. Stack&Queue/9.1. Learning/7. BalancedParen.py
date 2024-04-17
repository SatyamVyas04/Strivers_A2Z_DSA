def isValidParenthesis(s: str) -> bool:
    # Write your code here
    d = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or i != d[stack.pop()]:
            return False

    return len(stack) == 0

# Link: https://www.naukri.com/code360/problems/valid-parentheses_795104