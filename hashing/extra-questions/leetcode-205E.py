from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))

solution = Solution()
print(solution.isIsomorphic("fot","bar"))

# Results: 69.13% time (42 ms) 83.59% space(14.2MB)