"""
Input = [73, 74, 75, 71, 69, 72, 76, 73]
output = [1, 1, 4, 2, 1, 1, 0, 0]
Time/Space complexity = O(N)
"""
# Solution 1
class Solution(object):
    def dailyTemperatures(self, T):
        
        if not T:
            return None
        
        stack = []
        out = [0]*len(T)
        
        for i in range(len(T) - 1, -1, -1):            
            while stack and T[i] >= stack[-1][0]:
                stack.pop()
            
            if stack:
                out[i] = stack[-1][1] - i

            stack.append((T[i], i))
                
        return out



# Solution 2
"""
Time Complexity = O(N**2)
Space Complexity = O(N) 
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        if not T:
            return None
        
        out = []
        
        for indx, val in enumerate(T):
            found = False
            for i in range(indx + 1, len(T)):
                if val < T[i]:
                    found = True
                    out.append(i - indx)
                    break
            
            if not found:
                out.append(0)
                
        return out