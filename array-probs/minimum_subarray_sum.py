class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        start , s = 0,0
        l = 10**10
        
        for end in range(len(nums)):
            s += nums[end]
            
            while s >= target:
                l = min(l , end - start + 1)
                s -= nums[start]
                start += 1
        
        if l == 10**10:
            return 0
        return l
