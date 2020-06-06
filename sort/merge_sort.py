"""
Time complexity  = O(NlogN)
Space complexity = O(N)
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def divide(lst):
            if len(lst) == 1:
                return lst
            mid = len(lst)//2
            return merge(divide(lst[:mid]), divide(lst[mid:]))
        
        
        def merge(left, right):
            p1 = p2 = 0
            out = []
            while p1 < len(left) and p2 < len(right):
                if left[p1] > right[p2]:
                    out.append(right[p2])
                    p2 += 1
                else:
                    out.append(left[p1])
                    p1 += 1
            
            out.extend(left[p1:] or right[p2:])
            return out
        
        return divide(nums)