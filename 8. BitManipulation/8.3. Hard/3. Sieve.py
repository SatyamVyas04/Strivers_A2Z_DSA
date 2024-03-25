class Solution:
    def sieve(self, n: int) -> list[int]:
        sieve = [0]*(n)
        sieve[0] = 1
        sieve[1] = 1
        for i in range(2, n):
            if sieve[i] == 0:
                for j in range(i*i, n, i):
                    sieve[j] = 1
        return sieve

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        s = self.sieve(n)
        return s.count(0)

# Link: https://leetcode.com/problems/count-primes/