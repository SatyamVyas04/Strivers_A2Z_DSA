class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(n - 1):
            ans = self.recursive(ans)
            print(ans)
        return ans

    def recursive(self, string: str) -> str:
        ans = ""
        count = 1
        ptr = 0
        while ptr < len(string) - 1:
            if string[ptr] == string[ptr + 1]:
                ptr += 1
                count += 1
            else:
                ans += self.encode(string[ptr], count)
                ptr += 1
                count = 1
        ans += self.encode(string[-1], count)
        return ans

    def encode(self, n: str, count: int) -> str:
        return f"{count}{n}"

# Link: https://leetcode.com/problems/count-and-say/
