from typing import List
from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Keep count of all dest cities in each index. Remove if present within intermediate items in the path
        source = set(p[0] for p in paths)
        for path in paths:
            if path[1] not in source:
                return path[1]
solution = Solution()
print(solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

# Results: 26.84% time (67ms) 76.6% space (76.6%)