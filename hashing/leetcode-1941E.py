from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        approved_len = len(s)/len(freq)
        if approved_len%1 != 0:
            return False
        for c in freq:
            if freq[c] == approved_len:
                pass
            else:
                return False
        return True

class Solution2:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        freq = count.values()
        return len(set(freq)) == 1

solution = Solution()
print(solution.areOccurrencesEqual("abacbc"))

# Results: 86% time (32ms) 62.34% space (13.8MB)
# Model solution Results: 90.3% time (31ms), 22.63 % space (13.9MB)