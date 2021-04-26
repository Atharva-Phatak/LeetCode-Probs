class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        d = {}
        for x in arr:
            d[x] = d.get(x , 0) + 1
        
        p = 0
        count = 0
 
        for x in sorted(d.values() , reverse = True):
            p += x
            count += 1
            if p >= len(arr) // 2:
                return count 
