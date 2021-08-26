"""
Time Complexity = O(row*col)
Space Complexity = O(1)
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        out = []
        if not matrix:
            return out
        
        row, col = len(matrix), len(matrix[0])
        left = top = 0
        bottom = row - 1
        right = col - 1
        
        while (left <= right and top <= bottom):
            # Traverse right
            for c in range(left, right + 1):
                out.append(matrix[left][c])
                
            # Traverse down
            for r in range(top + 1, bottom + 1):
                out.append(matrix[r][right])
                
            if top != bottom:
                # Traverse left
                for c in range(right - 1, left - 1, -1):
                    out.append(matrix[bottom][c])
                    
            if left != right:
                # Traverse up
                for r in range(bottom - 1, top, -1):
                    out.append(matrix[r][left])
                    
            left += 1
            top += 1
            right -= 1
            bottom -= 1
                    
        return out