
import os
import sys
from copy import deepcopy
def input(): return sys.stdin.readline().rstrip("\r\n")


sys.setrecursionlimit(10 ** 7)


def insertionSort(arr, i):
    # write your code here !!!
    if i == len(arr):
        return
    else:
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    insertionSort(arr, i+1)


class Runner:
    def __init__(self):
        self.n = 0
        self.arr = []

    def takeInput(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))

    def execute(self):

        ans = insertionSort(self.arr, 0)

    def executeAndPrintOutput(self):
        ans = insertionSort(self.arr, 0)
        print(*self.arr)


runner = Runner()
runner.takeInput()
runner.executeAndPrintOutput()

# Link: https://www.codingninjas.com/studio/problems/insertion-sort_624381
