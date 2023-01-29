from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curr = ans = 0
        
        for x in nums:
            curr += x
            ans += counts[curr-k]
            counts[curr] += 1
            
        return ans
            
solution = Solution()
print(solution.subarraySum([1,2,1,2,1],3))

# Results: 87.94% time (300ms) 17.63% space (18.2MB)