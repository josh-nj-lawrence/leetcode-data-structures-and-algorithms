class Solution:
    def runningSum(self, nums):
        runningSum = [nums[0]]
        for i in range(1,len(nums)):
            runningSum.append(nums[i]+runningSum[-1])
        return runningSum

solution = Solution2()
print(solution.runningSum([1,2,3,4]))

# Results: 20.75% speed (84 ms) 23.43% (14.2 MB)