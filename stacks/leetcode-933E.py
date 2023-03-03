# FIFO implementation
from collections import deque

class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        self.counter.append(t)
        print(self.counter)
        while self.counter[0] < t-3000:
            self.counter.popleft()
        return len(self.counter)
    

obj = RecentCounter()
print(obj.ping(642))
print(obj.ping(1849))
print(obj.ping(4921))
print(obj.ping(5936))
print(obj.ping(5957))


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Results: 85.92% time (277ms) 48.12% space (19.5MB)