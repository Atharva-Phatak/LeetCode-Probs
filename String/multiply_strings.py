class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a , b = 0,0
        for d in num1:
            a = a * 10 + (ord(d) - ord('0'))
        for d in num2:
            b = b * 10 + (ord(d) - ord('0'))
            
        return str(a*b)
