"""
Time complexity = O(N)
Space Complexity = O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow, fast = head, head
        prev = None
        
        if not head:
            return True
        
        # Completed the halfway
        while fast and fast.next:
            fast = fast.next.next 
            temp = prev
            prev = slow
            slow = slow.next
            prev.next = temp
            
            
        if fast:
            slow = slow.next
            
        while prev and prev.val == slow.val:
            prev = prev.next
            slow = slow.next
            
        return not prev