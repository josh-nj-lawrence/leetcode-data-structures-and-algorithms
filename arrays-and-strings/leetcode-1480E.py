class Solution:
    def runningSum(self, nums):
        runningSum = [nums[0]]
        for i in range(1,len(nums)):
            runningSum.append(nums[i]+runningSum[-1])
        return runningSum

class Solution2:
    def runningSum(self, nums):
        ans = [0]*len(nums)
        ans[0] = nums[0]
        for i in range(1,len(nums)):
            ans[i] = nums[i]+ans[-1]
        return ans
solution = Solution2()
print(solution.runningSum([1,2,3,4]))

# Results: 20.75% speed (84 ms) 23.43% (14.2 MB)