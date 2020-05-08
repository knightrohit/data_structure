"""
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Time/Space complexity : O(N)
"""
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not image:
            return image
        
        if not image[0]:
            return image
        
        row, col = len(image), len(image[0])
        
        visited = set()
        queue = deque()
        color = image[sr][sc]
        queue.append((sr, sc))
        
        while queue:
            r, c = queue.pop()
            image[r][c] = newColor
            visited.add((r, c))
            #Move down
            if (r + 1, c) not in visited and r + 1 < row and image[r + 1][c] == color:
                queue.append((r + 1, c))
            
            # Move right
            if (r, c + 1) not in visited and c + 1  < col and image[r][c + 1] == color:
                queue.append((r, c + 1))                
            
            # Move left 
            if (r, c - 1) not in visited and c - 1 >= 0 and image[r][c - 1] == color:
                queue.append((r, c - 1))
                
            # Move up
            if (r - 1, c) not in visited and r - 1 >= 0 and image[r - 1][c] == color:
                queue.append((r - 1, c))
                
        return image 