from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pnt = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[pnt] == 0:
                nums[i], nums[pnt] = nums[pnt], nums[i]
            if nums[pnt] != 0:
                pnt +=1
                
lst = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(lst)
print(lst)

# Results: speed 43.48% (327 ms) space 58.31% (15.5 MB)