class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None]*k
        self.head = 0
        self.counter = 0
        self.capacity = k
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.counter == self.capacity:
            return False
        
        self.queue[(self.head + self.counter) % self.capacity] = value
        self.counter += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.counter == 0:
            return False
        
        self.head = (self.head + 1) % self.capacity
        self.counter -= 1
        return True
        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.counter == 0:
            return -1
        
        else:
            return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.counter == 0:
            return -1
        else:
            return self.queue[(self.head + self.counter - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.counter == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.counter == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()