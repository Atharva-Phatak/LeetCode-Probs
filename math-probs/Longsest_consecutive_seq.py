class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        l_streak = 1
        c_streak = 1
        nums.sort()
        for i in range(1 , len(nums)):
            
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    c_streak += 1
                else:
                    l_streak = max(l_streak , c_streak)
                    c_streak = 1
        
        return max(l_streak , c_streak)
