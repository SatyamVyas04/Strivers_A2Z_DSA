from typing import List


def letterCombinations(digits: str) -> List[str]:
    d = {'0': ['0'], '1': ['1'], '2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}

    ansarr = []

    def helper(s, idx, ds):
        if idx == len(s):
            ansarr.append(ds)
            return

        for letter in d[s[idx]]:
            ds += letter
            helper(s, idx + 1, ds)
            ds = ds[:-1]
    helper(digits, 0, "")
    return ansarr

# Link: https://www.codingninjas.com/studio/problems/letter-phone_626178