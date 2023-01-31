from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Count freq of loss per player
        freq = defaultdict(int)
        for x,y in matches:
            freq[x] = freq[x]
            freq[y] += 1
        ans = [[],[]]
        for x,y in sorted(freq.items()):
            if y == 0:
                ans[0].append(x)
            elif y == 1:
                ans[1].append(x)
        return ans

solution = Solution()
print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

# Results: 50.16% time (1999ms) 79.31% space (68.7MB)