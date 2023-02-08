from collections import Counter
from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        return max((count for count in counts if counts[count] == count), default=-1)

solution = Solution()
print(solution.findLucky([1,1,2,2,2,3,3]))

# Results: 76.40% time (59 ms) 90.70 % space (13.9MB)