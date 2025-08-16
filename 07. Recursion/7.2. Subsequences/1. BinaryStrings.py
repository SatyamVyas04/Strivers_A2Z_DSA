# def generateString(N: int) -> list[str]:
#     # write your code here
#     def genbin(n, bs):
#         if len(bs) == n:
#             if "11" not in bs:
#                 print(bs, end = " ")
#         else:
#             genbin(n, bs + '0')
#             genbin(n, bs + '1')
#     genbin(N, "")
#     print()
#     return []

"""
    Time Complexity: O(2^n)
    Space Complexity: O(n)

    Where 'n' is the length of the string to be created.
"""

from typing import List


def generateStringHelper(K: int, string: str, n: int, ans: List[str]):
    # Print binary string without consecutive 1's.
    if n == K:
        # Terminate binary string ans push it in answer.
        ans.append(string)
        return

    # If previous character is '1', then we put only '0' at the end of the string.
    if string[n - 1] == '1':
        string += '0'
        generateStringHelper(K, string, n + 1, ans)

    # If previous character is '0', then we put both '1' and '0' at the end of the string.
    if string[n - 1] == '0':
        string += '0'
        generateStringHelper(K, string, n + 1, ans)
        string = string[:-1] + '1'
        generateStringHelper(K, string, n + 1, ans)


def generateString(N: int) -> List[str]:
    ans = []
    if N == 0:
        return ans

    # A string with K elements.
    string = '0'
    # First character '0'.
    generateStringHelper(N, string, 1, ans)

    # First character '1'.
    string = '1'
    generateStringHelper(N, string, 1, ans)

    ans.sort()
    return ans

# Link: https://www.codingninjas.com/studio/problems/-binary-strings-with-no-consecutive-1s._893001
