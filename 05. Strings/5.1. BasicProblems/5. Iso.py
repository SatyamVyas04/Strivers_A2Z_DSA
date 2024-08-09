def areIsomorphic(s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False

    s2t, t2s = {}, {}
    for i in range(len(s)):
        if s[i] in s2t and s2t[s[i]] != t[i]:
            return False
        if t[i] in t2s and t2s[t[i]] != s[i]:
            return False
        s2t[s[i]] = t[i]
        t2s[t[i]] = s[i]
    return True

# Link: https://www.codingninjas.com/studio/problems/isomorphic-strings-_1117636