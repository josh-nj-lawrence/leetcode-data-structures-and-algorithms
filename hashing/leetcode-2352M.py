from typing import List
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, columns = defaultdict(int), defaultdict(int)
        ans = 0
        for row in grid:
            key = tuple(row)
            rows[key] +=1
        for col in range(len(grid[0])):
            curr = []
            for row in range(len(grid)):
                curr.append(grid[row][col])
            key = tuple(curr)
            columns[key] +=1

        for subarray in rows:
            ans += rows[subarray] * columns[subarray]
        return ans

solution = Solution()
print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

# Results: 79.7% time (533ms) 91.62 space (18.8MB)