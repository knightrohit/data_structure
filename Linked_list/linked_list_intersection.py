"""
Time complexity = O(m+n)
Space complexity = O(1)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        if headA == headB:
            return headA

        s_a = s_b = 0
        nodeA = headA
        nodeB = headB
        
        node = headA
        while node:
            s_a += 1
            node = node.next
            
        node = headB
        while node:
            s_b += 1
            node = node.next
            
        if s_a > s_b:
            diff = s_a - s_b
            while diff:
                nodeA = nodeA.next
                diff -= 1
                
        if s_b > s_a:
            diff = s_b - s_a
            while diff:
                nodeB = nodeB.next
                diff -= 1
                
        
        #Now both node are at the same level
        while nodeA and nodeB:
            if nodeA ==  nodeB:
                return nodeA
            
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next

        return None