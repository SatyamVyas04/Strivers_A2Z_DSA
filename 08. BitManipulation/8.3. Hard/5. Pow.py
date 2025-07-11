mod = int(1e9 + 7)


def power(N: int, R: int) -> int:
    # Write your code here.
    # Naive approach in below 2 lines, neglect it
    # ans = int(N**R)
    # return int(ans % mod)

    result = 1
    N = N % mod

    while R > 0:
        if R & 1:
            result = (result*N) % mod
        N = (N*N) % mod
        R >>= 1
    return result

# Link: https://www.codingninjas.com/studio/problems/power-of-numbers_8157729
