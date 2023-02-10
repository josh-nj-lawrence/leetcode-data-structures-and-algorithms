from typing import List
from collections import defaultdict 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
            ans = 0
        # Two pointer itterate over all contiguous sub arrays and add to ans if criteria is met 