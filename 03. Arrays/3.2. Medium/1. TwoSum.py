def read(n: int, book: list[int], target: int) -> str:
    # Write your code here.
    d = {}
    for i, num in enumerate(book):
        rem = target - num
        if rem in d.keys():
            return "YES"
        else:
            d[num] = i
    return "NO"

# Link: https://www.codingninjas.com/studio/problems/reading_6845742