import string
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l,r = 0,len(s)-1
        alphabet = list(string.ascii_letters)
        ans = list(s)
        while l<r:
            if ans[l] not in alphabet:
                l +=1
            if ans[r] not in alphabet:
                r -=1
            if ans[l] in alphabet and ans[r] in alphabet:    
                # swap
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
        return "".join(ans)

solution = Solution()
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))

# Results: 41.81 % speed ( 40 ms) 59.86% space (13.8 MB)