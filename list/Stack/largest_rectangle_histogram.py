"""
Input: [2,1,5,6,2,3]
Output: 10
Time/Space complexity = O(N)
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0
        
        stack = []
        max_area = 0
        
        for width, height in enumerate(heights):
            start = width
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                max_area = max(max_area, h*(width-idx))
                start = idx
                
            stack.append((start, height))
    
        for i, h in stack:
            max_area = max(max_area, h*(len(heights) - i))
            
        return max_area