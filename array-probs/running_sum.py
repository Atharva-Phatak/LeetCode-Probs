class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        current_sum = 0
        arr = []
        for ele in nums:
            current_sum += ele
            arr.append(current_sum)
        
        return arr
