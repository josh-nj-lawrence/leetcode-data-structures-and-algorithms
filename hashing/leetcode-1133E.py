from typing import List
from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        try:
            ans = max(n for n in counts if counts[n] ==1) 
        except ValueError:
            return -1
        return ans

solution = Solution()
print(solution.largestUniqueNumber([5,7,3,9,4,9,8,3,8,1]))

# Results: 85.42% time (47ms) 31.60% (14.1MB)