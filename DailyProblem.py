from collections import defaultdict


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n-1):
            cur_xor = arr[i]
            for k in range(i+1, n):
                cur_xor ^= arr[k]
                if cur_xor == 0:
                    ans += k - i
        return ans
