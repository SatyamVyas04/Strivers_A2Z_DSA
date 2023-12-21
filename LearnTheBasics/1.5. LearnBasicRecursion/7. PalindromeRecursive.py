def isPalindrome(string: str) -> bool:
    x = list(string)
    l2 = []
    def recur(x):
        if not x:
            return
        l2.append(x.pop())
        recur(x)
    recur(x)
    if string == "".join(l2):
        return True
    else:
        return False
    
# Link: https://www.codingninjas.com/studio/problems/check-palindrome-recursive_624386