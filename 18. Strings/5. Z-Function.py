def calculate_z(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r] == s[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r] == s[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z


def z_algorithm(pattern, text):
    combined = pattern + "$" + text
    z = calculate_z(combined)
    pattern_length = len(pattern)
    result = []
    for i in range(len(z)):
        if z[i] == pattern_length:
            result.append(i - pattern_length - 1)
    return result


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        zarr = z_algorithm(needle, haystack)
        if zarr:
            return zarr[0]
        return -1

# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
