def myPow(x: float, n: int) -> float:
    # Write your code here.
    if n < 0:
        x = 1 / x
        n = -n
    def recur(x, n, power):
        if n == 0:
            return power
        if n & 1:
            power *= x
        return recur(x*x, n>>1, power)
    return recur(x, n, 1)
    
# Link: https://www.codingninjas.com/studio/problems/find-x-raised-to-power-n-_626560