"""
Time/Space Complexity = O(N)
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        self.out = []
        
        def po(node):
            if not node:
                return

            self.out.append(str(node.val))
            if node.children:
                self.out.append(str(len(node.children)))
                for child in node.children:
                    po(child)
            else:
                self.out.append('0')
        po(root)
        return ','.join(self.out)
        
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        queue = deque(data.split(','))
        
        def deserializeHelper(queue):
            if queue:
                val = queue.popleft()
                if not val:
                    return None
                else:
                    node = Node(int(val), [])
                    childs = int(queue.popleft())
                    for _ in range(childs):
                        node.children.append(deserializeHelper(queue))                        
                return node
            return Node()
       
        return deserializeHelper(queue) if len(queue) > 0 else Node()
        