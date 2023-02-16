from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = Counter(s)
        ans = ""
        for c in order:
            if c in s:
                ans += c * s_counts[c]
                s_counts.pop(c)
        for c in s_counts.elements():
            ans += c
        return ans

solution = Solution()
print(solution.customSortString("cba","abcdz"))

#Results: 56.82% time (34ms) 98.6% space(13.8MB)