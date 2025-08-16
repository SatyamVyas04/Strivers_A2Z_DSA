def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    mini = prices[0]
    maxprofit = 0
    for i in range(1, len(prices)):
        profit = prices[i] - mini
        maxprofit = max(maxprofit, profit)
        mini = min(mini, prices[i])
    return maxprofit

# Link: https://www.codingninjas.com/studio/problems/best-time-to-buy-and-sell-stock_6194560
