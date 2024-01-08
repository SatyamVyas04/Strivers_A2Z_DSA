# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         short = min(strs, key=len)
#         for i, c in enumerate(short):
#             for other in strs:
#                 if other[i]!=c:
#                     return short[:i]
#         return short

class Solution:
    def longestCommonPrefix(self, inp: [str]) -> str:
        ans = ""
        n = len(inp)
        mini = len(min(inp, key=len))
        for i in range(mini):
            mainchar = inp[0][i]
            flag = 1
            for j in range(1, n):
                if inp[j][i] != mainchar:
                    flag = 0
                    break
            if flag:
                ans += mainchar
            else:
                return ans
        return ans
    
# Link: https://leetcode.com/problems/longest-common-prefix/