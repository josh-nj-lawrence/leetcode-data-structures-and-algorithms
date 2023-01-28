from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        ans = 0
        for x in arr:
            if x+1 in seen:
                ans +=1
        return ans

# Results: 50.93% time (47 ms) 14.86% space (14.1MB)
