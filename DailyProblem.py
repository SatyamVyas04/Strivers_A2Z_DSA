class Solution:
    def numTeams(self, rating) -> int:
        n = len(rating)
        ans = 0
        # ascend
        for i in range(1, n-1):
            cleft, cright = 0, 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    cleft += 1
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    cright += 1
            ans += cleft * cright

        # descend
        for i in range(1, n-1):
            cleft, cright = 0, 0
            for j in range(0, i):
                if rating[j] > rating[i]:
                    cleft += 1
            for j in range(i+1, n):
                if rating[i] > rating[j]:
                    cright += 1
            ans += cleft * cright
        return ans


sol = Solution()
print(sol.numTeams([2, 5, 3, 4, 1]))
