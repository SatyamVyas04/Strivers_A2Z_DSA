# class Solution:
#     def countGoodNumbers(self, n: int) -> int:
#         mod = 1000000007
#         odd = n//2
#         even = n//2 + n%2
#         return (self.binaryExp(5, even)%mod *self.binaryExp(4, odd)%mod)%mod

#     def binaryExp(self, x, n):
#         mod = 1000000007
#         if n==0:
#             return 1
#         if n < 0:
#             return 1/self.binaryExp(x, -n)

#         if n%2==0:
#             return self.binaryExp((x*x)%mod, n//2)
#         else:
#             return x * self.binaryExp((x*x)%mod, (n-1)//2)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Mathematical Problem Bruhhh
        # Say, 4 digits:
        # > Index 0: 5 choices -> Even
        # > Index 1: 4 choices -> Prime
        # > Index 2: Same as Index 0
        # > Index 3: Same as Index 1
        # Final Count: 5*4*5*4 -> 200

        # # Say, 5 digits:
        # Final Count: 5*4*5*4*5 -> 1000

        # if n & 1:
        #     return pow(5, n//2+1, 1000000007)*pow(4, n//2, 1000000007) % 1000000007
        # return pow(20, n//2, 1000000007)

        MOD = 10**9+7
        if n % 2 == 0:
            ne = n // 2
        else:
            ne = (n + 1) // 2
        no = n // 2
        te = pow(5, ne, MOD)
        tp = pow(4, no, MOD)
        return (tp * te) % MOD

# Link: https://leetcode.com/problems/count-good-numbers/
