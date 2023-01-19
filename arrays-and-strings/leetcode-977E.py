# Squares of a Sorted Array
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two Pointer, ignore negative signs
        i, j = 0, len(nums)-1
        ans = []
        while i<=j:
            if abs(nums[i]) < abs(nums[j]):
                ans.insert(0, nums[j]**2)
                j -=1
            else:
                ans.insert(0, nums[i]**2)
                i += 1
        return ans

solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))

# Results: 36.89% speed (428ms) 78.86% space (16.2 MB)

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        l,r = 0, len(nums)-1
        for i in reversed(range(len(nums))):
            if abs(nums[l]) < abs(nums[r]):
                result[i] = nums[r]**2
                r -=1
            else:
                result[i] = nums[l]**2
                l +=1
        return result


solution2 = Solution2()
print(solution2.sortedSquares([-4,-1,0,3,10]))

# Results: 62.69% speed (246ms) 45.99% space (16.3 MB)
# Time: O(n) Space O(n)

         