class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # Write your code here.
        mini = prices[0]
        maxprofit = 0
        for i in prices[1:]:
            maxprofit = max(maxprofit, i - mini)
            mini = min(mini, i)
        return maxprofit

# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
