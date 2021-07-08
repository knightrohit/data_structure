"""
Time/Space Complexity = O(N)
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        out = []
  
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    temp.append(node.val)                
                if node.children:
                    queue.extend(node.children)
                    
            out.append(temp)
 
        return out