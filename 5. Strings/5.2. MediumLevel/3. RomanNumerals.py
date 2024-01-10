def romanToInt(s:str) -> int:
    # Write your code here
    d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    currval = d[s[-1]]
    for i in range(len(s)-2, -1, -1):
        if d[s[i]] < d[s[i+1]]:
            currval -= d[s[i]]
        else:
            currval += d[s[i]]
    return currval

# Link: https://www.codingninjas.com/studio/problems/roman-numeral-to-integer_981308