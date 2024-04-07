class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []  # (idx, char)
        stars = []  # storing idx's
        for idx, ch in enumerate(s):
            if ch == "*":
                stars.append(idx)
            elif not stack:
                stack.append((idx, ch))
            elif ch == ")" and stack[-1][-1] == "(":
                stack.pop()
            else:
                stack.append((idx, ch))

        if not stack:
            return True
        elif len(stars) < len(stack):
            return False
        else:
            for idx, ch in stack:
                if ch == "(":
                    stars_ahead = list(filter(lambda x: x > idx, stars))
                    if stars_ahead:
                        stars.remove(stars_ahead[0])
                    else:
                        return False
                else:
                    stars_before = list(filter(lambda x: x < idx, stars))
                    if stars_before:
                        stars.remove(stars_before[0])
                    else:
                        return False
            return True
