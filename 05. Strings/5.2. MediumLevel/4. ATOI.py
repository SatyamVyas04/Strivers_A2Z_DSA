from typing import Optional

def createAtoi(s: str) -> int:
    # write your code here
    INT_MAX =  2147483647
    INT_MIN = -2147483648

    s = s.strip()

    if s.isnumeric():
        if int(s) > INT_MAX:
            return INT_MAX
        if int(s) < INT_MIN:
            return INT_MIN
        return int(s)
    if s == "":
        return 0

    sign = "-" if s[0] == "-" else ""
    ans = sign + ""

    for i in range(0, len(s)):
        if (s[i] == "-" or s[i] == "+") and i == 0:
            continue
        if s[i].isnumeric():
            ans += s[i]
        else:
            break

    if ans == "-" or ans == "":
        return 0
    if int(ans) > INT_MAX:
        return INT_MAX
    if int(ans) < INT_MIN:
        return INT_MIN
    return int(ans)

# Link: https://www.codingninjas.com/studio/problems/implement-atoi-function_981270