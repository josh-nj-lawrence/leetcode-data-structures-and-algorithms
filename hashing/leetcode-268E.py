from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        included = set()
        for n in nums:
            included.add(n)
        mx = len(nums)
        for i in range(0,mx):
            if i not in included:
                return i
        return mx
        
solution = Solution()
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))

# Results: 46.51% time (171ms) 7.4% space (15.8 MB)