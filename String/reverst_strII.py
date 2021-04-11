class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        x = ""
        idx = 0
        while idx < len(s):
            
            x += s[idx : idx + k][::-1] + s[idx + k : idx + 2*k]
            idx += 2*k
        
        return x
