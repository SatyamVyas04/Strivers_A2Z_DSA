class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, target, arr, n):
        ans = 0
        ratio = []
        for item in arr:
            ratio.append((item.value, item.weight))
        ratio = sorted(ratio, key=lambda x: x[0]/x[1], reverse=True)
        for value, weight in ratio:
            if weight <= target:
                ans += value
                target -= weight
            else:
                ans += target/weight * value
                break
        return ans

# Link: https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1