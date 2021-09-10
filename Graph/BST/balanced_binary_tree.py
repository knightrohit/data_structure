"""
Time/Space Complexity = O(N)
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.balance = True

        def chk(node):
            if not self.balance:
                return -1
            
            if not node:
                return 0
            
            left = chk(node.left)
            right = chk(node.right)
            
            if abs(left-right) > 1:
                self.balance = False
                return -1
            
            return max(left, right) + 1
        
        chk(root)
        return self.balance