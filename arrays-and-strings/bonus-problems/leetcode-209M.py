from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Edge cases
        if sum(nums) < target:
            return 0
        # Produce Prefix Sum array for O(1) speed for subarray sum
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        # Itterate over subarray sizes
        size = 0
        while True:
            l= 0
            size +=1
            print(size)
            r = l + size
            while r < len(nums):
                if prefix[r]-prefix[l] >= target:
                    return size
                l += 1
                r += 1
            

solution = Solution()
print(solution.minSubArrayLen(15,[1,2,3,4,5]))

# Not full coverage