class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        total_len = len(s)
        return (ones - 1)*"1" + (total_len - ones)*"0" + "1"