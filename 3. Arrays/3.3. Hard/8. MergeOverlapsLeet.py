class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort()
        ans = [intervals.pop(0)]
        for i in intervals:
            if not ans or ans[-1][-1] < i[0]:
                ans.append(i)
            else:
                ans[-1][-1] = max(ans[-1][-1], i[-1]) 
        return ans
    
# Link: https://leetcode.com/problems/merge-intervals/