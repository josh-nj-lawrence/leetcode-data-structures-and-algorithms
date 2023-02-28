class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for x in s:
            if stack:
                if stack[-1] == x:
                    #Pop and don't add x
                    stack.pop()   
                else: 
                    stack.append(x)
            else:
                stack.append(x)
            
        return "".join(stack)
    
sol = Solution()
print(sol.removeDuplicates("abbaca"))

# Results: 97.98% time (62ms) 75.89 % space (14.8MB)