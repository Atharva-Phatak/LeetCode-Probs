import collections 
        
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        d = collections.defaultdict(int)
        for char in s:
            d[char] += 1
        
        count = 0
        for char in t:
            if d[char]:
                d[char] -= 1
            
            else:
                count +=1
        
        return sum(d.values())
