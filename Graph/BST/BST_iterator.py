"""
Time/Space Complexity = O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_inorder(root)

    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            if node.right:
                self.left_inorder(node.right)
            return node.val

    def hasNext(self) -> bool:
        return self.stack
        
    def left_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left