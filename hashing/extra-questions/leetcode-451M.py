from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        ans = ""
        for k,v in counts.most_common(len(counts.keys())):
            ans += k*v 
        return ans

solution = Solution()
print(solution.frequencySort("aassjdkjkjkjslkdjlfkjalskdfljasjdfl"))

# Results: 94.20% time (36ms) 73.13% space (15.2MB)