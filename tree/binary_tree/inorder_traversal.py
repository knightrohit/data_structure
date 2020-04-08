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