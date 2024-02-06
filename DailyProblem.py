class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in d.keys():
                d[key] = [i]
            else:
                l = d[key]
                l.append(i)
                d[key] = l
        return list(d.values())
