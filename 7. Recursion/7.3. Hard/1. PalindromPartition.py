from typing import List


def partition(s: str) -> List[List[str]]:
    from typing import List
    ans = []
    ds = []
    n = len(s)

    def help(ind):
        if ind == n:
            ans.append(ds[:])
            return
        for i in range(ind, n):
            s1 = s[ind:i+1]
            if s1 == s1[::-1]:
                ds.append(s1)
                help(i+1)
                ds.pop()
    help(0)
    return ans

# Link: https://www.codingninjas.com/studio/problems/palindrome-partitioning_626181
