"""
Implement Linkedlist with below methods
get
addAtHead
addAtTail
addAtIndex
deleteAtIndex
"""

class LinkedList:
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LinkedList(None)
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        
        node = self.head.next
        while index > 0:
            node = node.next
            index -= 1
        return node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = LinkedList(val)
        node.next = self.head.next
        self.head.next = node        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        i = self.size
        node = self.head.next
        while i > 1:
            node = node.next
            i -= 1
        node.next = LinkedList(val)           
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        temp = LinkedList(val)
        
        if index == 0 and self.size == 1:
            temp.next = self.head.next
            self.head.next = temp
            self.size += 1
            return
        elif index == 0 and self.size == 0:
            self.head.next = temp
            self.size += 1
            return
            
        node = self.head.next
        while index > 1:
            node = node.next
            index -= 1
            
        temp.next = node.next
        node.next = temp
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        
        if index == 0 and self.size <= 1:
            self.head.next = None
            self.size -= 1
            return

        elif index == 0:
            self.head.next = self.head.next.next
            self.size -= 1
            return

        node = self.head.next
        while index > 1:
            node = node.next
            index -= 1
            
        node.next = node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)