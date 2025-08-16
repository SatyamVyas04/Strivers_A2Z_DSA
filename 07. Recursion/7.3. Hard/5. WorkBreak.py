def getAllValidSentences(s: str, worddict: list[str]) -> list[str]:
    # Write your code here
    res = []

    def helper(current_string, ans_string):
        if len(current_string) == 0:
            res.append(ans_string.strip())
            return
        for i in range(0, len(current_string)):
            left = current_string[:i+1]
            right = current_string[i+1:]
            if left in worddict:
                helper(right, ans_string+left+" ")

    helper(current_string=s, ans_string="")
    return res

# Link: https://www.codingninjas.com/studio/problems/word-break-1_758963
