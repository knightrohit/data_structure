"""
nums = [0,1,2,2,3,0,4,2], val = 2,
out = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0
        
        if val == None:
            return len(nums)
        
        curr_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr_pos] = nums[i]
                curr_pos += 1
        # Pop remaining elements as those were already copied        
        for _ in range(len(nums) - curr_pos):
            nums.pop()
            
        return curr_pos