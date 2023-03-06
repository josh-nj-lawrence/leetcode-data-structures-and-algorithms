from collections import deque
class StockSpanner:

    def __init__(self):
        self.stack = [] # Store a monotonically decreasing value stack of price, answer pairs

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Results: 81.84% time (417ms) 32.89% space (19.6MB)