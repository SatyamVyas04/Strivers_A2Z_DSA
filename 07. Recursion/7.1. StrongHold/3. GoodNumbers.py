from typing import List


def goodNumbers(a: int, b: int, digit: int) -> List[int]:
    arr = []
    for i in range(a, b+1):
        if str(digit) in str(i):
            continue
        i = str(i)
        index = len(i) - 2
        flag = 1
        while index > -1:
            if int(i[index]) <= sum(map(int, i[index+1:])):
                flag = 0
            index = index-1
        if flag:
            arr.append(int(i))
    return arr

# Link: https://www.codingninjas.com/studio/problems/good-numbers_625508
