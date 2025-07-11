class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        ans = 0
        heights = [0]*len(matrix[0])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    heights[col] += int(matrix[row][col])
                else:
                    heights[col] = 0
            ans = max(ans, self.findTallestRect(heights))
        return ans

    def findTallestRect(self, heights: list[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights)+1):
            while stack and ((i == len(heights)) or (heights[stack[-1]] >= heights[i])):
                height = heights[stack[-1]]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1]-1
                ans = max(ans, width*height)
            stack.append(i)
        return ans

# Link: https://leetcode.com/problems/maximal-rectangle/
