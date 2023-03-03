from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # monotonically decreasing stack
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
            
sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

# Results: 98.14% time (1317ms) 77.3% space (28.4MB)