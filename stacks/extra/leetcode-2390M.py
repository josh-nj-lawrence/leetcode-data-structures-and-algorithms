class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for x in s:
            if stack and x == "*":
                stack.pop()
            else:
                stack.append(x)
        return "".join(stack)
    
sol = Solution()
print(sol.removeStars("leet**cod*e"))

# Results: 56.6% time (241ms) 39.86% space (15.6MB)