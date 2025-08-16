# def moreSubsequence(n: int, m: int, a: str, b:str) -> str:
#     # Write your code here.
#     c1 = len(set(generateSubsequences(a)))
#     c2 = len(set(generateSubsequences(b)))
#     if c1 > c2:
#         return a
#     return b

# def generateSubsequences(s:str) -> [str]:
#     # Write your code here.
#     ans = []
#     def gen(curr, s, n, a):
#         if curr == n:
#             return
#         if curr == n - 1:
#             ans.append(a)
#             ans.append(a + s[n-1])
#             return
#         gen(curr+1, s, n, a)
#         gen(curr+1, s, n, a+s[curr])

#     n = len(s)
#     gen(0, s, n, "")
#     return ans

"""
    Time Complexity: O(N+M)
    Space Complexity: O(N+M)

    where 'N' and 'M' are the length of the strings.
"""


def func(s: str, n: int) -> int:
    # Initializing 'count' with 1.
    count = 1

    # Creating a dictionary 'm1' to store character counts.
    m1 = {}

    # Calculating the number of distinct subsequences.
    for i in range(n):
        if s[i] not in m1:
            m1[s[i]] = count
            count *= 2
        else:
            temp = m1[s[i]]
            m1[s[i]] = count
            count *= 2
            count -= temp

    return count


def moreSubsequence(n: int, m: int, a: str, b: str) -> str:
    if func(a, n) >= func(b, m):
        return a
    else:
        return b

# Link: https://www.codingninjas.com/studio/problems/more-subsequence_8842355
