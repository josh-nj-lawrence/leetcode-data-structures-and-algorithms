from collections import COunter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = l = r = 0
        sub = Counter()
        
        while r < len(s):
            right = s[r]
            sub[r] += 1
            while sub[r] > 1:
                left = s[l]
                sub[l] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans 

# Results: 45.12% time (92 ms) 91.28% space (14MB)