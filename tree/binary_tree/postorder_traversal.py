#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS Recursive solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.out = []
        
        def traverse(node):
            
            if node == None:
                return None
            
            traverse(node.left)
            traverse(node.right)
            self.out.append(node.val)           
        
        traverse(root)
        return self.out


#Iterative solution
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, out = [], []
        
        if not root:
            return out
        
        stack.append(root)
        while stack:
            node = stack.pop()
            out.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)            
            
        return out[::-1] 