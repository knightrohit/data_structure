"""
Time/Space Complexity = O(N)
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 < len(nums):
            node.right = self.sortedArrayToBST(nums[mid+1:])
        return node