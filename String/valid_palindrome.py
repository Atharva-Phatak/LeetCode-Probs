import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.replace(" ","").lower()
        s = "".join([x for x in s if x not in string.punctuation])
        
        return s == s[::-1]
