from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointer, start left and right and swap them until they meet or cross
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i +=1
            j -=1

solution = Solution()
s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)

# Results: 44.6% speed (226 ms) 17.94% space (18.5MB)
