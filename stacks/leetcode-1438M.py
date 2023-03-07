from collections import deque
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Maxdeq being monotonically decreasing (stores max in first index) and min being opposite
        maxdeq, mindeq = deque(), deque()
        l = ans = 0

        for r in range(len(nums)):
            # Maintain queues
            while maxdeq and maxdeq[-1] < nums[r]:
                maxdeq.pop()
            while mindeq and mindeq[-1] > nums[r]:
                mindeq.pop()
            # Append new val
            maxdeq.append(nums[r])
            mindeq.append(nums[r])

            # Check if condition is met
            while maxdeq[0]- mindeq[0] > limit:
                #Conditionally pop off queues
                if nums[l] == maxdeq[0]:
                    maxdeq.popleft()
                if nums[l] == mindeq[0]:
                    mindeq.popleft()
                l += 1
            ans = max(ans, r-l+1)
            
        return ans

sol = Solution()
print(sol.longestSubarray([8,2,4,7],4))

# Results: 81.13 % time (659ms) 98.21% space(23.2MB)