class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights) + 1):
            while stack and ((i == len(heights)) or (heights[stack[-1]] >= heights[i])):
                height = heights[stack[-1]]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                ans = max(ans, width * height)
            stack.append(i)
        return ans

# Better Approach: Area = Curr_Height * (NextSmallerIndex - PrevSmallerIndex - 1)

# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
