from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1
        
        for c in ransomNote:
            if letters[c] == 0:
                return False
            letters[c] -= 1
        return True

sol = Solution()
print(sol.canConstruct("aa","ab"))

# Results: 55.89% time (69ms) 48.44% space (14.2MB) 