from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge Cases
        n = len(nums)
        if n*k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_queue(i):
            # Enforce queue size
            if queue and queue[0] == i-k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
        
        queue = deque()
        max_id = 0

        # Init ans array with initialization of first grouping
        for i in range(k):
            clean_queue(i)
            queue.append(i)
            if nums[i] > nums[max_id]:
                max_id = i
        ans = [nums[max_id]]

        print(queue)
        # Itter over rest of array for ans
        for i in range(k,n):
            clean_queue(i)
            queue.append(i)
            ans.append(nums[queue[0]])
            print(queue, ans)

        return ans
            

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

# Results: 82.69% time (1717ms) 89.8% space (29.8MB)