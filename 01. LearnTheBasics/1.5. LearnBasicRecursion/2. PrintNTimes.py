def printNtimes(n: int) -> None:
    if n==0:
        return
    else:
        printNtimes(n-1)
        print("Coding Ninjas", end=" ")
        
# Link: https://www.codingninjas.com/studio/problems/-print-n-times_8380707