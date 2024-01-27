class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        m = 10**9+7
        prev = [0] * (k+1)
        prev[0] = 1

        for N in range(1, n+1):
            curr = [0] * (k+1)
            total = 0  # Sliding Window
            for K in range(k+1):
                if K >= N:
                    total -= prev[K-N]
                total += prev[K]
                curr[K] = total % m
            prev = curr
        return prev[k]
