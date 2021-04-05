class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        m = set()
        for ele in arr:
            if 2*ele in m or 0.5*ele in m:
                return True
            m.add(ele)
        
        return False
