class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Modify nums in-place instead.
        """        
        if not nums:
            return []
        
        if len(nums) == 1:
            return nums
        
        p1 = 0 
        p2 = 1
        
        while p2 < len(nums):
            
            if nums[p2] != 0 and nums[p1] == 0:
                nums[p1] = nums[p2]
                nums[p2] = 0
                p2 += 1
                p1 += 1
                
            elif nums[p1] == 0 and nums[p2] == 0:
                p2 += 1
            
            elif nums[p1] != 0 and nums[p2] == 0:
                p1 += 1
                p2 += 1
                
            else:
                p1 += 1
                p2 += 1
                
        return nums