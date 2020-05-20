"""
Time complexity = O(N)
Space complexity = O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        new_tail = head
        new_head = head
        
        while new_tail.next:
                if new_head == new_tail:
                    new_head = new_tail.next
                    new_tail.next = new_tail.next.next
                    new_head.next = new_tail
                    
                else:
                    temp_head = new_tail.next
                    new_tail.next = new_tail.next.next
                    temp_head.next = new_head
                    new_head = temp_head
                    
        return new_head