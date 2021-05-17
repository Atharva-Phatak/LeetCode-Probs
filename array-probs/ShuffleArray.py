class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        z = []
        for i , j in zip(nums[:n] , nums[n:]):
            z.extend([i,j])
        
        return z
