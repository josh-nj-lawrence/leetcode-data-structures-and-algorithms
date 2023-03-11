class Solution:
    def robotWithString(self, s: str) -> str:
        # 
        n = len(s)
        m = [0]*n+[s[n-1]] # Will store a list of vals from s which shares ascending lexicographical order such that after popped to the paper it's lexicographically correct
        
        for i in range(n-1,-1,-1):
            if s[i] < m[i+1]:
                m[i] = s[i]
            else:
                m[i] = m[i+1]
        
        t, p = [], []
        for i in range(n):
            t.append(s[i])
            while t and t[-1] <= m[i+1]:
                p.append(t.pop())
        while t:
            p.append(t.pop())
        return "".join(p)
    
sol = Solution()
print(sol.robotWithString("bac"))

# Result: 87.37% time (742ms) 26.77% space (17.9MB)