class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        l,r = 0,k
        count,ans = 0,0

        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            if r-l+1 == k:
                if count > ans:
                    ans = count
                if s[l] in vowels:
                    count-=1
                l+=1
        return ans
solution = Solution()
print(solution.maxVowels('weallloveyou', 7))

# Results: time 70.77 % (199ms) space 15.54% (15MB)