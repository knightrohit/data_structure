# dfs recursion solution
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.out = []
        def traversal(node):
            if not node:
                return None

            self.out.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return self.out


# Iterative solution using stack
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, out = [], []
        
        if root == None:
            return out
        
        stack.append(root)
        while stack:
            node = stack.pop()
            out.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)            
        return out