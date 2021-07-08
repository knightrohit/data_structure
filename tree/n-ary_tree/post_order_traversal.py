"""
Time/Space Complexity = O(N)
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Using recursion
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.out = []
        
        def po(node):
            if node:
                if node.children:
                    for children in node.children:
                        po(children)
                
                self.out.append(node.val)
                
        po(root)
        return self.out