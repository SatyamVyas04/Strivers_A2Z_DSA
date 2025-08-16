class Solution:
    def minPartition(self, N):
        notes = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        notes.reverse()
        count, amt = 0, N
        arr = []
        for note in notes:
            if note <= amt:
                count = amt // note
                for _ in range(count):
                    arr.append(note)
                amt %= note
        return arr

# Link: https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
