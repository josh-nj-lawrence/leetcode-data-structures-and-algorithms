from collections import Counter
from typing import List
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(count for count in counts if counts[count] == 1)

solution = Solution()
print(solution.sumOfUnique([1,2,3,2,4]))

# Results:  39.53% time (41ms) 94.2% space (13.8MB)
