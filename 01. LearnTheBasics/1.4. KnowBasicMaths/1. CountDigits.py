def countDigits(n: int) -> int:
    digits = str(n)
    count = 0
    for i in digits:
        if int(i) == 0:
            continue
        if n%int(i) == 0:
            count+=1
    return count

# Link: https://www.codingninjas.com/studio/problems/count-digits_8416387