class MyQueue:

    def __init__(self):
        self.queue = []
        self.reversal = []

    def push(self, x: int) -> None:
        if self.reversal:
            # Then reversal contains reversal of queue, reverse and append
            self.reorder()    
        self.queue.append(x)
        
            
    def pop(self) -> int:
        # Edge Case of empty queue
        if self.empty():
            return None
        # Need to pop from reversal
        if self.queue:
            # Then queue contains records
            self.reverse()
        return self.reversal.pop()
        

    def peek(self) -> int:
        if self.empty():
            return None
        if self.queue:
            return self.queue[0]
        else:
            return self.reversal[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0 and len(self.reversal) == 0
        
    # Helper functions
    def reorder(self) -> None:
        while self.reversal:
            self.queue.append(self.reversal.pop())

    def reverse(self) -> None:
        while self.queue:
            self.reversal.append(self.queue.pop())

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj.pop())
print(obj.peek())
print(obj.empty())

# Results: 69.20% time (31 ms) 13.74 % space (14.1MB)