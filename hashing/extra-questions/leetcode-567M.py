from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        l1 = len(s1)
        for i,c in enumerate(s2):
            c2[c] += 1
            if i >= l1:
                c2[s2[i-l1]] -= 1
            if c1 == c2:
                    return True
        return False
            
solution = Solution()
print(solution.checkInclusion("ab","eidbaooo"))

# Results: 47.11% time (107ms) 93.3% space (13.9MB)