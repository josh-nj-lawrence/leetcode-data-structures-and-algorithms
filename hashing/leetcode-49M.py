from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["a"]))

# Results: 96.92% time (91ms) 95.68%