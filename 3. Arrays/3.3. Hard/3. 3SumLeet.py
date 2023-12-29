class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        res = set()

        # Spliting
        n, p, z = [], [], []
        for i in nums:
            if i>0:
                p.append(i)
            elif i<0:
                n.append(i)
            else:
                z.append(i)

        N, P = set(n), set(p)

        # Case1: p, 1z, n
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        
        # Case2: 0, 0, 0
        if len(z)>=3:
            res.add((0,0,0))

        # Case 3: 2 negatives == 1 positive
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                t = -1*(n[i] + n[j])
                if t in P:
                    res.add(tuple(sorted([n[i], n[j], t])))

        # Case 4: 2 positive == 1 negative
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                t = -1*(p[i] + p[j])
                if t in N:
                    res.add(tuple(sorted([p[i], p[j], t])))

        return res

# Link: https://leetcode.com/problems/3sum/