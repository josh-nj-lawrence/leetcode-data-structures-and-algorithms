from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []
        stack = []
        tmp = 0
        for x in heights[::-1]:
            if not stack:
                stack.append(x)
                tmp += 1
                ans.append(0)
            else:
                while stack and x>stack[-1]:
                    stack.pop()
                    tmp += 1
                if not stack:
                    tmp -= 1
                stack.append(x)
                ans.append(tmp)
                tmp = 1
        return ans[::-1]

sol = Solution()
print(sol.canSeePersonsCount([3,1,5,8,6]))

# Results: 89.19% time (1153ms) 38.65% space (29.7MB)