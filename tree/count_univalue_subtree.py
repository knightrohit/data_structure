"""
Time/Space Complexity: O(N)
"""
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.total = 0
        
        def po(node):
            if not node:
                return node
            
            left = po(node.left)
            right = po(node.right)
            
            if (left and right and left == right == node.val) or (not left and right and right == node.val) or(left and not right and left == node.val) or (not left and not right) :
                self.total += 1
                return node.val
            
            return 'x'
        
        po(root)
        return self.total