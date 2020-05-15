
"""
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
output = [3,9,20,null,null,15,7]
"""
# Recursion solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not inorder or not postorder:
            return None

        node = TreeNode(postorder.pop())        
            
        node_partition = inorder.index(node.val)
        # Please make sure to run the right node call first to build the stack for left node
        node.right = self.buildTree(inorder[node_partition+1:], postorder)
        node.left = self.buildTree(inorder[:node_partition], postorder)        
        return node