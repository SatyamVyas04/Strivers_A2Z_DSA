n = int(input())
digits = list(str(n))
size = len(digits)

for i in digits:
    n -= int(i)**size
    
if n:
    print("false")
else:
    print("true")
    
# Link: https://www.codingninjas.com/studio/problems/check-armstrong_589