from typing import List
from collections import Counter 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        ans = 0
        counts = Counter()
        for x in prefix:
            ans += counts[x]
            counts[x+goal] += 1
        return ans

solution = Solution()
print(solution.numSubarraysWithSum([1,0,1,0,1], goal = 2))

# Results: 60.35% time (310ms) 5.89% space (19MB)