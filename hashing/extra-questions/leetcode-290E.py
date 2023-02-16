from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        p_s_map = defaultdict()
        s_p_map = defaultdict()
        for c, w in zip(pattern, s.split()):
            if c not in p_s_map:
                if w in s_p_map:
                    return False
                p_s_map[c] = w
                s_p_map[w] = c
            if p_s_map[c] != w:
                return False
        return True
    
solution = Solution()
print(solution.wordPattern("abba","dog dog dog dog"))

# Results: 55.15% time (33ms) 61.1% space (13.8 MB)