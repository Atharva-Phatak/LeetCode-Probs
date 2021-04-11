class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        a , b = 0 , 0
        for s in num1:
            a = a*10 + (ord(s) - ord('0'))
        
        for s in num2:
            
            b = b *10 + (ord(s) - ord('0'))
        
        return str(a + b)
