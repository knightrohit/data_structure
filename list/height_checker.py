"""
Time Complexity = O(Nlog(N))
Space Complexity = O(N)
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:       
        return [i != j for i, j in zip(heights, sorted(heights))].count(True)