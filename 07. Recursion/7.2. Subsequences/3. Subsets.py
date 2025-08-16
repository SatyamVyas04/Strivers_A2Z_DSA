from typing import List


def generateSubsequences(s: str) -> List[str]:
    # Write your code here.
    ans = []

    def gen(curr, s, n, a):
        if curr == n:
            return
        if curr == n - 1:
            ans.append(a)
            ans.append(a + s[n-1])
            return
        gen(curr+1, s, n, a)
        gen(curr+1, s, n, a+s[curr])

    n = len(s)
    gen(0, s, n, "")
    return ans

# Link: https://www.codingninjas.com/studio/problems/print-subsequences_8416366
