from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = [] 
        ans = [0]*len(nums)-k+1
        l,r = 0,k-1
        # Create monotonically increasing stack which holds the indecies of values in nums which are strictly increasing 
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1]:
                
            stack.append(i)

            

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
