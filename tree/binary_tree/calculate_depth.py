#Recursive solution
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        level = 0
        self.answer = 0
        def traverse(node, level):
            if node == None:
                return None

            traverse(node.left, level+1)
            traverse(node.right, level+1)
            self.answer = max(self.answer, level)
        
        traverse(root, level+1)        
        return self.answer