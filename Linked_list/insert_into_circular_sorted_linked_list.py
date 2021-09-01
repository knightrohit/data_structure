"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        
        prev, curr = head, head.next
        insert = False
        
        while True:
            if prev.val <= insertVal <= curr.val:
                insert = True
            # Add at the end
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    insert = True
                    
            if insert:
                prev.next = Node(insertVal, curr)
                #prev.next = node
                return head
            
            prev, curr = curr, curr.next
            if prev == head:
                break
                
        prev.next = Node(insertVal, curr)
        return head