from typing import List


# Link: https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494
def minSubsetSumDifference(arr: List[str], n: int) -> int:
    k = sum(arr)
    lastRow = subsetSumToK(n, k, arr)
    ans = float("inf")
    for partition1 in range(0, k//2 + 1):
        if lastRow[partition1]:
            ans = min(ans, abs(2 * partition1 - k))
    return ans


# Link: https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954
def subsetSumToK(n, k, arr):
    if n == 0:
        return False

    dp = [[False for _ in range(k + 1)] for _ in range(n)]

    # All indices at 0 target -> True
    for i in range(0, n):
        dp[i][0] = True

    # 0th indices, when target is arr[0] -> True
    if arr[0] <= k:
        dp[0][arr[0]] = True

    for index in range(1, n):
        for target in range(1, k + 1):
            notTake = dp[index-1][target]
            take = False
            if arr[index] <= target:
                take = dp[index-1][target-arr[index]]
            dp[index][target] = take or notTake

    # slight variation here
    return dp[n-1]
