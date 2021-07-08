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


# Iteration
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        self.out, self.stack = [], [root]
        
        while self.stack:
            node = self.stack.pop()
            if node:
                self.out.append(node.val)
            if node.children:
                self.stack.extend(node.children)
                
        return self.out[::-1]