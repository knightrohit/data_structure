"""Find missing element in O(1) space and O(n) time, [1,n]"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        if len(nums) == 1:
            return nums        
        
        out = []
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] = nums[abs(i) -1] * -1                
        
        for i in range(len(nums)):            
            if nums[i] > 0:
                out.append(i+1)           
                
        return out