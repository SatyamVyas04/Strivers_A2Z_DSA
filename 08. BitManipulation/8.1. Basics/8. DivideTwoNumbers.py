def divideTwoInteger(A: int, B: int) -> int:
    # write your code here
    if (A == -2147483648 and B == -1):
        return 2147483647
    a, b, res = abs(A), abs(B), 0
    for x in range(32)[::-1]:
        if (a >> x) - b >= 0:
            res += 1 << x
            a -= b << x
    return res if (A > 0) == (B > 0) else -res


# Logic:
    # if (a >> x) - b >= 0:
    #     if a divided by 2, x times is still greater than b, we move ahead
    #
    # a -= b << x
    #     the if statement above implies that b can be multiplied at most by 2, x times. Their remainder is made the new a
    #
    # res += 1 << x
    #     because b was multiplied by 2 x times, that is the quotient buff

# Example 14 and 3
    # at x == 2, a>>x becomes 14/2 -> 7/2 -> 3 which is >= 3
    # now b << x becomes 3 << 2 -> 12
    # and 1 << x becomes 4 because we multiplied 3 technically with 4
    # so 1 << x is added to the result and a becomes remained, a -= b << x


# Link: https://www.codingninjas.com/studio/problems/-divide-two-integers_1112617?leftPanelTabValue=SUBMISSION
