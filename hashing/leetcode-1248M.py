from collections import defaultdict
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Use curr to track prefix sum for odd numbers, add to dict and use same intuition for differences in count dict
        count = defaultdict(int)
        count[0] = 1
        curr = ans = 0
        for x in nums:
            curr += x % 2
            ans += count[curr-k]
            count[curr] += 1
        return ans 

# Results: 86.28% time (837ms) 19.93% space (23.1MB)