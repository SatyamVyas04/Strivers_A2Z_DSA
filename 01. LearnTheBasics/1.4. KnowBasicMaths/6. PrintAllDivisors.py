def sumOfAllDivisors(n: int) -> int:
    # ans = 0
    # for i in range(1, n+1):
    #     ans += i*(n//i)
    # return ans

    ans = 0
    l = 1

    # Iterating over all values of 'l' such that 'n/l' is distinct.
    # There at most 2*sqrt(n) such values.
    while l <= n:
        val = n // l

        # 'r' = maximum value of 'i' such that 'n/i' is val.
        r = n // val
        ans += ((r * (r + 1)) // 2 - (l * (l - 1)) // 2) * val

        # moving on to next range.
        l = r + 1

    return ans

# Link: https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720
