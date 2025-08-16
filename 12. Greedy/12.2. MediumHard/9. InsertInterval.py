class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = []
        for i in intervals:
            if not ans:
                ans.append(i)
            else:
                lasts, laste = ans[-1]
                currs, curre = i
                if currs <= laste:
                    ans[-1] = [min(lasts, currs), max(curre, laste)]
                else:
                    ans.append(i)
        return ans

# Link: https://leetcode.com/problems/insert-interval/
