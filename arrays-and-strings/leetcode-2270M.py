from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[-1])

        n = len(nums)
        for i in range(len(nums)-1):
            if (prefix[i]) >= (prefix[n-1]-prefix[i]):
                ans +=1
        return ans
solution = Solution()
print(solution.waysToSplitArray([10,4,-8,7]))

# Results: 77.65% (972 ms) 77.39% space (28.7 MB)