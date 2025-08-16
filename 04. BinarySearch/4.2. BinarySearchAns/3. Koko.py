from math import ceil


def minimumRateToEatBananas(v: [int], h: int) -> int:
    # Write Your Code Here.
    low = 1
    high = max(v)
    ans = float("inf")
    while low <= high:
        mid = (low + high) // 2
        totalhrs = hourlyTotal(v, mid)
        if totalhrs <= h:
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    return ans


def hourlyTotal(v: [int], mid: int) -> int:
    total = 0
    for i in v:
        total += ceil(i/mid)
    return total

# Link: https://www.codingninjas.com/studio/problems/minimum-rate-to-eat-bananas_7449064
