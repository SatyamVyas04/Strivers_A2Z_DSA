from typing import List


def commonPrefix(inp: List[str], n: int) -> str | int:
    # Write your code here
    ans = ""
    mini = len(min(inp, key=len))
    for i in range(mini):
        mainchar = inp[0][i]
        flag = 1
        for j in range(1, n):
            if inp[j][i] != mainchar:
                flag = 0
                break
        if flag:
            ans += mainchar
        else:
            return ans if ans != "" else -1
    return ans if ans != "" else -1

# Link: https://www.codingninjas.com/studio/problems/longest-common-prefix_628874
