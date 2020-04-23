"""Input: [ [ 1, 2, 3 ],  [ 4, 5, 6 ],  [ 7, 8, 9 ] ]
Output:  [1,2,4,7,5,3,6,8,9]
"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix or not matrix[0]:
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        
        out, temp = [], []
        for d in range(row+col-1):
            
            r = 0 if d < col else d - col + 1
            c = d if d < col else col - 1
            
            while r < row and c >= 0:
                temp.append(matrix[r][c])
                r += 1 
                c -= 1                
            
            if d % 2 == 0:
                temp.reverse()
                out.extend(temp)
                
            else:
                out.extend(temp)
            temp.clear() 
                
        return out