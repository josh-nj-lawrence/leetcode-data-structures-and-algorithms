class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        l, r = 0,0
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                r = i
                while l<=r:
                    word[r], word[l] = word[l], word[r]
                    r -= 1
                    l += 1
                return "".join(word)

solution = Solution()
print(solution.reversePrefix("abcdefd","d"))

# Result: time 32.1% (42 ms) space 55.92% (13.8 MB), at most O(n+n) time and O(1) space 