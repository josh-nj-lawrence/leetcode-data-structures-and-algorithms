from typing import List
from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        ans = []
        length = len(nums)
        for arr in nums:
            for x in arr:
                freq[x] += 1
        for key in freq:
            if freq[key] == length:
                ans.append(key)
        return sorted(ans)

solution = Solution()
print(solution.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))

# Results: 61.88% time (76ms) 90.42 % space (14.2MB)
        