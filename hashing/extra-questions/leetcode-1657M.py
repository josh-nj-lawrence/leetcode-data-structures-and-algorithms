from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1_count = Counter(word1)
        w2_count = Counter(word2)
        if sorted(w1_count.values()) == sorted(w2_count.values()) and set(word1) == set(word2):
            return True
        return False
    
solution = Solution()
print(solution.closeStrings("uau", "ssx"))

# Results: 69.24% time (152ms) 18.82% space (15.4MB)