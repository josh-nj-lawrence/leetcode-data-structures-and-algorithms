class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Implement two pointer to see if we can delete elements in s to produce t
        i, j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1 
                j +=1
            else:
                j +=1
        if i == len(s):
            return True
        else:
            return False

# Results: 84.28 % runtime (32 ms) 36.98 % space (13.9 MB)
# O(n+m) runtime O(1) space (just pointers)

# Model Solution
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i< len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# Results: 46.40 % runtime (43 ms) 98.91 % space )13.8 MB
