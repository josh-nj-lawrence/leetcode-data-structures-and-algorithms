from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque(maxlen=size)        
        self.summation = 0
        self.len = 0
        self.maxlen = size

    def next(self, val: int) -> float:
        if self.len < self.maxlen:
            self.len += 1
        else:
            self.summation -= self.queue.popleft()
        
        self.summation += val
        self.queue.append(val)

        return self.summation/self.len

sol = MovingAverage(3)
print(sol.next(1))
print(sol.next(2))
print(sol.next(3))
print(sol.next(10))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Results 1: 44.27% time (104ms) 69.20% space (17.2MB)
# Results 2: 83.57% time (66ms) 69.20% space (17.2MB)