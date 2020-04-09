Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.out = []        
        
        def traverse(node):

            if not node:
                return None

            traverse(node.left)
            self.out.append(node.val)
            traverse(node.right)
            
        traverse(root)        
        return self.out


# Iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        out, stack = [], []
        
        if not root:
            return self.out
         
        node = root
        
        while (node or stack):
         
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            out.append(node.val)
            node = node.right
            
        return out