from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurances = []
        for count in counts.values():
            if count in occurances:
                return False
            occurances.append(count)
        return True

solution = Solution()
print(solution.uniqueOccurrences([1,2,2,1,1,2,3]))

# Results: 49.31% time (43ms) 66.70% space(13.9MB)