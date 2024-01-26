# class Solution:
#     def addOperators(self, num: str, target: int) -> list[str]:
#         exp = []
#         for i in num:
#             exp.append(i)
#             exp.append("_")
#         exp.pop()
#         ans = []

#         def helper(idx):
#             if exp.count("_") == 0:
#                 string = "".join(exp)
#                 if eval(string) == target:
#                     ans.append(string)
#                 return

#             if exp[idx] == "_":
#                 exp[idx] = "+"
#                 helper(idx+2)
#                 exp[idx] = "-"
#                 helper(idx+2)
#                 exp[idx] = "*"
#                 helper(idx+2)
#                 exp[idx] = "_"

#         helper(1)
#         return ans


# sol = Solution()
# print(sol.addOperators("232", 8))

# Failed 105 case where we can have 1*0+5 and 10-5
# how tf do I get that 10

class Solution:
    def addOperators(self, num, target):
        def dfs(l, r, expr, cur, last, res):
            if l == r:
                if cur == target:
                    res.append(expr)
                return
            for i in range(l + 1, r + 1):
                if i == l + 1 or (i > l + 1 and num[l] != "0"):  # prevent "00"
                    s, x = num[l:i], int(num[l:i])
                    if last == None:
                        dfs(i, r, s, x, x, res)
                    else:
                        dfs(i, r, expr+"+"+s, cur + x, x, res)
                        dfs(i, r, expr+"-"+s, cur - x, -x, res)
                        dfs(i, r, expr+"*"+s, cur-last+last*x, last*x, res)

        res = []
        dfs(0, len(num), '', 0, None, res)
        return res

# Link: https://leetcode.com/problems/expression-add-operators/