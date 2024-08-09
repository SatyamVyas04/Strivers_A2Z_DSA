class Solution:
    def largestOddNumber(self, num: str) -> str:
        if num[-1] in ["1", "3", "5", "7", "9"]:
            return num
            
        ind = len(num) - 1
        while ind > -1:
            if int(num[ind])%2 == 1:
                return num[:ind+1]
            ind -= 1
        return ""
    
# Link: https://leetcode.com/problems/largest-odd-number-in-string/