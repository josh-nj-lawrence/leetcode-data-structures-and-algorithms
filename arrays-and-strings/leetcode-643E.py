from typing import List 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = ans =  sum(nums[:k])
        for i in range(len(nums)-k):
            curr = curr - nums[i] + nums[i+k]
            ans = max(ans, curr)
        return ans/k

solution = Solution()
print(solution.findMaxAverage([5], 1))

# Results: 92.33 % time (1220 ms) and 51.27% space (26.1 MB)