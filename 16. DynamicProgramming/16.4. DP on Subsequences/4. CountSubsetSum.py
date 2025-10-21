from typing import List
from math import pow


def findWays(arr: List[int], k: int) -> int:
    MOD = 1000000007
    n = len(arr)
    if n == 0:
        return 0

    zeroCount = arr.count(0)
    arr = [x for x in arr if x != 0]  # remove zeros for DP
    n = len(arr)

    dp = [[0 for _ in range(k + 1)] for _ in range(n)]

    # Base case: target 0 is always achievable (empty subset)
    for i in range(n):
        dp[i][0] = 1

    # Base case: first element
    if arr[0] <= k:
        dp[0][arr[0]] = 1

    for index in range(1, n):
        for target in range(1, k + 1):
            notTake = dp[index - 1][target]
            take = 0
            if arr[index] <= target:
                take = dp[index - 1][target - arr[index]]
            dp[index][target] = (take + notTake) % MOD

    # Account for zeros (each zero doubles the number of ways)
    return (dp[n - 1][k] * int(pow(2, zeroCount))) % MOD

# Link: https://www.naukri.com/code360/problems/number-of-subsets_3952532
