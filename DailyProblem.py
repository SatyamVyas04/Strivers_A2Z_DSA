class Solution:
    def maxLength(self, arr: [str]) -> int:
        dp = [set()]
        for word in arr:
            letters = set(word)
            if len(letters) != len(word):
                continue
            for soln in dp:
                if soln & letters:
                    continue
                dp.append(soln | letters)
        return len(max(dp, key=len))

sol = Solution()
print(sol.maxLength(["ab","cd","cde","cdef","efg","fgh","abxyz"]))