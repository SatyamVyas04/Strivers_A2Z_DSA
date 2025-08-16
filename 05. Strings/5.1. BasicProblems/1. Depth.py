def maxDepth(s: str) -> int:
    # Write your code here.
    depth = 0
    ans = 0
    for i in s:
        if i == "(":
            depth += 1
            ans = max(ans, depth)
        if i == ")":
            depth -= 1
    return ans

# Link: https://www.codingninjas.com/studio/problems/maximum-nesting-depth-of-the-parentheses_8144741
