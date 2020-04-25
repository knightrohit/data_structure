""" Input: [1,4,3,2]
Output: 4 = > 4 = min(1, 2) + min(3, 4)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        if not nums:
            return nums
        
        if len(nums) == 2:
            return min(nums)
        
        nums.sort()
        n = len(nums)//2
        p1 = p2 = None
        sum_val = 0
        indx = 0
        for _ in range(n):
            p1 = nums[indx]
            p2 = nums[indx + 1]
            sum_val += min(p1, p2)
            indx += 2
            
        return sum_val