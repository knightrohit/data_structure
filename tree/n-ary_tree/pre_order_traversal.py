"""
Time/Space Complexity = O(N)
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.out = []
        
        def po(node):
            if node:
                self.out.append(node.val)
                if node.children:
                    for child_node in node.children:
                        po(child_node)
                
        po(root)
        return self.out


# Iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.out, self.stack = [], []

        if not root:
            return self.out
        
        self.stack.append(root)
        
        while self.stack:
            node = self.stack.pop()
            self.out.append(node.val)
            if node.children:
                self.stack.extend(node.children[::-1])
                
        return self.out