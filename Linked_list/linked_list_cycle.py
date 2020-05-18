"""
Time/Space Compexity = O(N)
"""
def hasCycle(head):
    
    if not head or not head.next:
        return False
    
    visited = set()
    node = head.next
    
    while node:
        node = node.next
        if node in visited:
            return True
        else:
            visited.add(node)
            
    return False
        

"""
Time Compexity = O(N)
Sapce complexity = O(1)
"""
def hasCycle(head):
    sp = head
    fp = head.next
    
    while sp != fp:
        if fp == None or fp.next == None:
            return False
        sp = sp.next
        fp = fp.next.next
        
    return True