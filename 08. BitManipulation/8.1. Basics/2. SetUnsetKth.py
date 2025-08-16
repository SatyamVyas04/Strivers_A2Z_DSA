def isKthBitSet(n: int, k: int) -> bool:
    # Write your code from here.
    return bool(n >> (k-1) & 1)

# Link: https://www.codingninjas.com/studio/problems/check-whether-k-th-bit-is-set-or-not_5026446
