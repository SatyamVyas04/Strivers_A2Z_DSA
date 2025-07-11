class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        res = []
        stack = []
        n = len(A)

        for i in range(n):
            while stack and stack[-1] >= A[i]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(A[i])
        return res

# Link: https://www.interviewbit.com/problems/nearest-smaller-element/
