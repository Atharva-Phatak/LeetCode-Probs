class Solution:
    
    @staticmethod
    def search_pairs(arr , target_sum , left , triplets):
        
        right = len(arr) - 1
        while left < right:
            
            current_sum = arr[left] + arr[right]
            
            if current_sum == target_sum:
                triplets.append([-target_sum , arr[left] , arr[right]])
                
                left += 1
                right -= 1
                
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                
                while left <right and arr[right] == arr[right + 1]:
                    right -= 1
            
            elif current_sum > target_sum:
                right -= 1
            else:
                left += 1
        
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        nums.sort()
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            self.search_pairs(nums , -nums[i] , i +1 ,triplets)
            #print(triplets)
        
        return triplets
