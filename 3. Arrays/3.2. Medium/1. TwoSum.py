def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    d = {}
    for i, n in enumerate(book):
        rem = target - n
        if rem in d.keys():
            return "YES"
        else:
            d[n] = i
    return "NO"

# Link: https://www.codingninjas.com/studio/problems/reading_6845742