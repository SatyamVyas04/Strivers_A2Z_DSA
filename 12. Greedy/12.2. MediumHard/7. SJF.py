class Solution:
    def solve(self, bt):
        bt.sort()
        wait = 0
        curr = 0
        for i in bt:
            wait += curr
            curr += i
        return int(wait/len(bt))


sol = Solution()
print(sol.solve([7, 1, 6, 9, 2, 10, 7, 7, 10, 9]))

# Link: https://www.geeksforgeeks.org/problems/shortest-job-first/1