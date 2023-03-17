class MedianFinder:

    def __init__(self):
        self.stack = [] # Use of queue allows for later implementation of pruning the data stream structure based on other logic
        self.size_of_queue = 0
        self.middle = 0 # Index which stores center element or left center element

    def addNum(self, num: int) -> None:
        # Need to add number to data structure to maintain order
        i = self.size_of_queue//2
        self.queue.append(num)
        # Need to take care of size and middle vals
        
        self.size_of_queue += 1
        # Only shift middle 
        if self.size_of_queue % 2 == 1:
            self.middle += 1
        print(self.middle, self.queue, self.size_of_queue)

    def findMedian(self) -> float:
        if self.size_of_queue % 2 == 1:
            return self.queue[self.middle-1]
        else:
            return (self.queue[self.middle-1]+self.queue[self.middle])/2
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())