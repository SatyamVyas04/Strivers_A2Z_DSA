from typing import List
from math import pow


# Prerequisite 1: Subset Sum Count
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


# The Problem
def countPartitions(n: int, d: int, arr: List[int]) -> int:
    ans = 0
    total = sum(arr)
    # 1. s1 + s2 = total
    # 2. s2 - s1 = d
    # Hence, we can say that
    # -> s2 - (total - s2) = d
    # -> 2s2 = total - d
    # -> s2 = (total - d) // 2
    # Hence, just the previous question
    # but finding s2

    # Edge cases to check for
    if (total - d) % 2 == 1 or (total - d) < 0:
        return 0

    s2 = (total - d) // 2
    return findWays(arr, s2)

# Link: https://www.naukri.com/code360/problems/partitions-with-given-difference_3751628
