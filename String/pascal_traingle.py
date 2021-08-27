"""
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        out = [[1]]
        row = 1
        while row < numRows:
            temp = []
            for i in range(row + 1):
                first = out[row - 1][i - 1] if i > 0 else 0 
                second = out[row - 1][i] if i < row else 0
                temp.append(first + second)
            row += 1
            out.append(temp)    
        return out