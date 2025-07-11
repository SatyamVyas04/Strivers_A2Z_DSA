class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        MOD = 10**9 + 7
        PRIME = 101
        
        def hashfn(s, length):
            hashval = 0
            for i in range(length):
                hashval = (hashval * PRIME + ord(s[i])) % MOD
            return hashval
        
        def updatehash(hashval, old, new, length):
            hashval = (hashval - ord(old) * pow(PRIME, length - 1, MOD)) % MOD
            hashval = (hashval * PRIME + ord(new)) % MOD
            return hashval
        
        min_repeats = (len(b) + len(a) - 1) // len(a)
        repeated_a = a * min_repeats

        if b not in repeated_a:
            repeated_a += a
        
        len_b = len(b)
        hash_b = hashfn(b, len_b)
        hash_window = hashfn(repeated_a[:len_b], len_b)

        for i in range(len(repeated_a) - len_b + 1):
            if hash_window == hash_b and repeated_a[i:i+len_b] == b:
                return min_repeats + (i + len_b > len(a) * min_repeats)
            if i + len_b < len(repeated_a):
                hash_window = updatehash(hash_window, repeated_a[i], repeated_a[i+len_b], len_b)
        
        return -1

# Link: https://leetcode.com/problems/repeated-string-match/submissions/1511474996/