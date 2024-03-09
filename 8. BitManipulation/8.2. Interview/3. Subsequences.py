def subsequences(string):
    ans = []
    length = 1 << len(string)
    for i in range(1, length):
        current_num = bin(i)[2:].zfill(len(string))
        current_str = return_int_to_str(string, current_num)
        ans.append(current_str)
    return ans


def return_int_to_str(string: str, num: str):
    ans = ""
    for i in range(len(string)):
        if num[i] == "1":
            ans += string[i]
    return ans

# Link: https://www.codingninjas.com/studio/problems/subsequences-of-string_985087?leftPanelTabValue=SUBMISSION
