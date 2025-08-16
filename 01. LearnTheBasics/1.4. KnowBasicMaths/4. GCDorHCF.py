def calcGCD(n: int, m: int) -> int:
    while m % n != 0:
        remainder = m % n
        m = n
        n = remainder
    return n

# Link: https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448
