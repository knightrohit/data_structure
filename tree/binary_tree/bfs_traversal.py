# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        out = []
        queue = deque()
        queue.append(root)
       
        while queue:
            out_temp = []
            queue_temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                out_temp.append(node.val)
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
                    
            out.append(out_temp)
            queue.extend(queue_temp)
            
        return out


# Reduced space complexity O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        out = []
        queue = deque()
        queue.append(root)
        
        level = 0
        while queue:
            out.append([])
            queue_len = len(queue)
            
            for _ in range(queue_len):
                node = queue.popleft()
                out[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return out