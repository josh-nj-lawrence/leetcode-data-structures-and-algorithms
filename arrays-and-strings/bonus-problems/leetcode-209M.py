from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,curr,size,ans = 0,0,len(nums), len(nums)+1
        for i in range(size):
            curr += nums[i]
            while curr >= target and l<=i:
                ans = min(ans, i+1-l)
                curr -= nums[l]
                l+=1
        return ans if ans != len(nums)+1 else 0
            

solution = Solution()
print(solution.minSubArrayLen(15,[1,2,3,4,5]))

# Results are good