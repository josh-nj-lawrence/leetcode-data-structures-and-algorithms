from typing import List
from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        digitsums = defaultdict(list)
        
        for num in nums:
            digitsum = sum(int(c) for c in str(num))
            digitsums[digitsum].append(num)
        # Itterate over digitsums and find max sum of two elements
        for key in digitsums:
            subarray = digitsums[key]
            if len(subarray) > 1:
                subarray.sort()
                ans = max(subarray[-1] + subarray[-2], ans)
        return ans

solution = Solution()
print(solution.maximumSum([18,43,36,13,7]))

# Results: 59.64% time (1334ms) 83.89% space (29MB)