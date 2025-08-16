class Solution:
    def partition(self, s: str) -> List[List[str]]:
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

# Link: https://leetcode.com/problems/palindrome-partitioning/description/
