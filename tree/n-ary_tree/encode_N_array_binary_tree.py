"""
Time Complexity = O(N)
Space Complexity = O(L)
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        
        if not root:
            return None
        
        rootNode = TreeNode(root.val)
        queue = deque([(rootNode, root)])
        
        
        while queue:
            
            prevBNode = None
            headBNode = None
            
            parent, curr = queue.popleft()
            
            for child in curr.children:
                new_node = TreeNode(child.val)
                
                if prevBNode:
                    prevBNode.right = new_node
                else:
                    headBNode = new_node
                
                prevBNode =  new_node
                queue.append((new_node, child))
                    
            parent.left = headBNode
            
        return rootNode            
                
            
        
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        
        if not data:
            return None
        
        rootNode = Node(data.val, [])
        queue = deque([(rootNode, data)])
        
        while queue:
            parent, current = queue.popleft()
            
            firstchild = current.left
            sibling = firstchild
            
            while sibling:
                new_node = Node(sibling.val, [])
                parent.children.append(new_node)
                queue.append((new_node, sibling))
                sibling = sibling.right
        return rootNode