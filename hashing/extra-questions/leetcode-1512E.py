from typing import List 
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        for number in counts:
            ans += counts[number] * (counts[number]-1)//2
        return ans

# Results: 94.73% time (28ms) 7.29% space (14MB)