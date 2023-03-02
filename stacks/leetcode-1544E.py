class Solution:
    def makeGood(self, s: str) -> str:
        stack = [x for x in s]
        print(stack)
        keepLooking  = True
        while keepLooking:
            keepLooking = False
            z = len(stack)-1
            for i in range(z):
                print("".join(stack), stack[i], stack[i+1], z, i)
                if (stack[i].isupper() and stack[i+1].islower() or stack[i].islower() and stack[i+1].isupper()) and (stack[i].lower() == stack[i+1].lower()):
                    # Delete and break out of for loop
                    stack.pop(i), stack.pop(i)
                    keepLooking = True
                    break
            if not keepLooking:
                return "".join(stack)

sol = Solution()
print(sol.makeGood("aAbBcC"))

# Results: 5.22% (91 ms) 10.66% space (14 MB)