class Solution:
    def sumSubarrayMins(self, A: list[int]) -> int:
        A = [0]+A
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)

# Link: https://leetcode.com/problems/sum-of-subarray-minimums/
# https://www.youtube.com/watch?v=z5folSN5wk8
