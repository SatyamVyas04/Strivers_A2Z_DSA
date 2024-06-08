class Solution:
    def findCelebrity(self, n: int) -> int:
        ans = 0
        for i in range(1, n):
            if knows(ans, i): # type: ignore
                ans = i
        for i in range(n):
            if ans != i:
                if knows(ans, i) or not knows(i, ans): # type: ignore
                    return -1
        return ans
    
# Find the Celebrity: https://www.geeksforgeeks.org/the-celebrity-problem/