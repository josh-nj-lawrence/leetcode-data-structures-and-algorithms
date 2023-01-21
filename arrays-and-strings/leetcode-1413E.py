from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Create prefix sum
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
        start = 0
        while True:
            start +=1
            ans = True
            for i in range(len(prefix)):
                if start + prefix[i] < 1:
                    ans = False
            if ans:
                return start
    
solution = Solution()
print(solution.minStartValue([-3,2,-3,4,2]))   

# Results: 31.22% time (58ms) 95.58% space (13.7MB)
