from typing import List
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indicies = defaultdict(List)
        for i in range(len(cards)):
            indicies[cards[i]].append(i)
        ans = float("inf")
        for key in indicies:
            arr = indicies[key]
            for i in range(len(arr)-1):
                ans = min(ans, arr[i+1] - arr[i] + 1)
        return ans if ans < float("inf") else -1

# Results: 34.52% time (1089ms) 13.83% space (42.8MB)