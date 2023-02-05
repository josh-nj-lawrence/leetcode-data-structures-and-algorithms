from collections import defaultdict
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if counts[num] > 1:
                return True
        return False

# Results: 31.87% time (598ms) 5.33% space (31.4 MB)